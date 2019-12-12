(ns dec02
    (:require [clojure.string :as str])
    (:require [clojure.math.combinatorics :as combo]))

(defn parse-file [file-name]
    (vec (map read-string (str/split (slurp file-name) #","))))

(defn parse-instruction [n]
  [(mod n 100)
   (int (/ (mod n 1000) 100))
   (int (/ (mod n 10000) 1000))
   (int (/ (mod n 100000) 10000))])

(defn positive-position [_ position] (pos? position))

(defn read-from [program position mode]
  (case mode
    0 (nth program (nth program position))
    1 (nth program position)))

(defn write-to [program position value]
  (let [pos (nth program position)]
    (assoc program pos value)))

(defn run [program position inputs]
    (loop [program program
           position position
           output (first inputs)
           inputs inputs]
        (let [[op-code mode-a mode-b mode-c]
                (parse-instruction (read-from program position 1))
              [program' position' output' inputs' done]
            (case op-code
                99 [program position output inputs true]

                1 [(write-to program (+ position 3)
                        (+
                        (read-from program (+ position 1) mode-a)
                        (read-from program (+ position 2) mode-b)))
                    (+ position 4)
                    output inputs false]

                2 [(write-to program (+ position 3)
                        (*
                        (read-from program (+ position 1) mode-a)
                        (read-from program (+ position 2) mode-b)))
                    (+ position 4)
                    output inputs false]

                3 [(write-to program (+ position 1) (first inputs))
                    (+ position 2)
                    output (rest inputs) false]

                4 [program
                    (+ position 2)
                    (read-from program (+ position 1) mode-a)
                    inputs true]

                5 [program
                    (if (= (read-from program (+ position 1) mode-a) 0)
                        (+ position 3)
                        (read-from program (+ position 2) mode-b))
                    output inputs false]

                6 [program
                    (if (= (read-from program (+ position 1) mode-a) 0)
                        (read-from program (+ position 2) mode-b)
                        (+ position 3))
                    output inputs false]

                7 [(write-to program (+ position 3)
                        (if (<
                            (read-from program (+ position 1) mode-a)
                            (read-from program (+ position 2) mode-b))
                        1 0))
                    (+ position 4)
                    output inputs false]

                8 [(write-to program (+ position 3)
                        (if (=
                            (read-from program (+ position 1) mode-a)
                            (read-from program (+ position 2) mode-b))
                        1 0))
                    (+ position 4)
                    output inputs false])]
            (if done
                {:program program'
                 :position position'
                 :output output'
                 :done (= op-code 99)}
                (recur program' position' output' inputs')))))

(defn run-amps [program phases]
    (loop [s0 (run program 0 [(nth phases 0) 0])
           s1 (run program 0 [(nth phases 1) (:output s0)])
           s2 (run program 0 [(nth phases 2) (:output s1)])
           s3 (run program 0 [(nth phases 3) (:output s2)])
           s4 (run program 0 [(nth phases 4) (:output s3)])]
        (if (:done s4)
            (:output s4)
            (let [s0' (run (:program s0) (:position s0) [(:output s4)])
                  s1' (run (:program s1) (:position s1) [(:output s0')])
                  s2' (run (:program s2) (:position s2) [(:output s1')])
                  s3' (run (:program s3) (:position s3) [(:output s2')])
                  s4' (run (:program s4) (:position s4) [(:output s3')])]
                (recur s0' s1' s2' s3' s4')))))

(defn find-max [program phases]
    (->> (combo/permutations phases)
         (map #(run-amps program %))
         (reduce max)))

(let [program (parse-file "input.amp")]
    (println "Part 1:" (find-max program [0 1 2 3 4]))
    (println "Part 2:" (find-max program [5 6 7 8 9])))

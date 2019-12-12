(ns dec02
    (:require [clojure.string :as str]))

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

(defn handle-position [program position input output]
    (let [[op-code mode-a mode-b mode-c] (parse-instruction (nth program position))]
        (let [[program' position' output'] (case op-code
          99 [program -1 output]
          1 [(write-to program (+ position 3)
                (+
                  (read-from program (+ position 1) mode-a)
                  (read-from program (+ position 2) mode-b)))
              (+ position 4)
              output]
          2 [(write-to program (+ position 3)
                (*
                  (read-from program (+ position 1) mode-a)
                  (read-from program (+ position 2) mode-b)))
              (+ position 4)
              output]
          3 [(write-to program (+ position 1) input)
             (+ position 2)
             output]
          4 [program
             (+ position 2)
             (read-from program (+ position 1) mode-a)]
          5 [program
             (if (= (read-from program (+ position 1) mode-a) 0)
               (+ position 3)
               (read-from program (+ position 2) mode-b))
             output]
          6 [program
             (if (= (read-from program (+ position 1) mode-a) 0)
               (read-from program (+ position 2) mode-b)
               (+ position 3))
             output]
          7 [(write-to program (+ position 3)
                (if (<
                     (read-from program (+ position 1) mode-a)
                     (read-from program (+ position 2) mode-b))
                  1 0))
             (+ position 4)
             output]
          8 [(write-to program (+ position 3)
                (if (=
                     (read-from program (+ position 1) mode-a)
                     (read-from program (+ position 2) mode-b))
                  1 0))
             (+ position 4)
             output])]

      [program' position' output'])))

(defn run-program [program input]
      (loop [program program position 0 output 0]
          (let [[program' position' output'] (handle-position program position input output)]
            (if (neg? position')
              output'
              (recur program' position' output')))))

(let [program (parse-file "program.testcode")]        
    (println "Part 1:" (run-program program 1)))

(let [program (parse-file "program.testcode")]        
    (println "Part 2:" (run-program program 5)))

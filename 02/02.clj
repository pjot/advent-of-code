(ns dec02
    (:require [clojure.string :as str])
    (:require [clojure.math.combinatorics :as combo]))

(defn parse-file [file-name]
    (vec (map read-string (str/split (slurp file-name) #","))))

(defn handle-position [program position]
    (let [op-code (nth program position)]
        (if (= op-code 99)
            [program -1]
            (let [a (nth program (nth program (+ position 1)))
                  b (nth program (nth program (+ position 2)))
                  c-position (nth program (+ position 3))
                  value (case op-code
                    1 (+ a b)
                    2 (* a b))]
                [(assoc program c-position value)
                 (+ position 4)]))))

(defn positive-position [_ position] (pos? position))

(defn run-program [program]
    (first
        (loop [program program position 0]
            (if (neg? position)
                program
            (let [[program' position'] (handle-position program position)]
                (recur program' position'))))))

(defn run-for [program noun verb]
    (run-program (assoc program 1 noun 2 verb)))

(defn run-until [program goal]
    (let [
        noun-verb
        (first (filter
            #(= (run-for program (first %) (second %)) goal)
            (combo/selections (range 99) 2)))]
        (+ (second noun-verb) (* 100 (first noun-verb)))))

(let [program (parse-file "program.intcode")]        
    (println "Part 1:" (run-for program 12 2))
    (println "Part 2:" (run-until program 19690720)))
(ns dec01
  (:use [clojure.string :only [split-lines]]))

(defn parse-file [file-name]
    (map read-string (split-lines (slurp file-name))))

(defn fuel-for-mass [mass]
    (- (int (/ mass 3)) 2))

(defn total-fuel-for-mass [mass]
    (reduce +
        (take-while pos? (rest (iterate fuel-for-mass mass)))))

(let [masses (parse-file "masses.txt")]        
    (println "Part 1:" (reduce + (map fuel-for-mass masses)))
    (println "Part 2:" (reduce + (map total-fuel-for-mass masses))))
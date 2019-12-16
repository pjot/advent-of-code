(ns dec16
  (:require [clojure.string :as string]))

(defn parse-offset [f]
  (as-> (slurp f) $
    (string/split-lines $)
    (first $)
    (subs $ 0 7)
    (Integer/parseInt $)))

(defn parse-file [f repeats]
  (as-> (slurp f) $
    (string/split-lines $)
    (first $)
    (apply str (seq (repeat repeats $)))
    (string/split $ #"")
    (map #(Integer/parseInt %) $)
    (vec $)))

(defn multipliers-for-phase-implementation [phase]
  (vec
   (concat
    (repeat phase 0)
    (repeat phase 1)
    (repeat phase 0)
    (repeat phase -1))))

(def multipliers-for-phase (memoize multipliers-for-phase-implementation))

(defn get-mod [coll i]
  (nth coll (mod i (count coll))))

(defn multiply-by-multipliers [multipliers]
  (fn [i n]
    (* n (get-mod multipliers (inc i)))))

(defn sum-for-multipliers [numbers multipliers]
  (as-> (multiply-by-multipliers multipliers) $
    (map-indexed $ numbers)
    (reduce + $)
    (Math/abs $)
    (mod $ 10)))

(defn apply-phase [numbers]
  (vec
   (map
    #(sum-for-multipliers numbers (multipliers-for-phase (inc %)))
    (range (count numbers)))))

(defn build-phase [acc curr]
  (conj acc (+ (last acc) curr)))

(defn apply-phase-fast [numbers]
  (->> (reverse numbers)
       (reduce build-phase [0])
       (rest)
       (reverse)
       (map #(mod % 10))
       (vec)))

(defn first-8 [numbers]
  (string/join
   (map str (take 8 numbers))))

(comment
  (println "Part 1:"
           (->> (parse-file "input.txt" 1)
                (iterate apply-phase)
                (take 101)
                (last)
                (first-8))))

(def offset (parse-offset "small.txt"))

(println
 (->> (parse-file "small.txt" 100)
      (iterate apply-phase-fast)
      (take 101)
      (last)
      (reverse)
      (first-8)))

(comment
  (println "Part 2:"
           (subs
            (string/join
             (->> (parse-file "small.txt" 100)
                  (iterate apply-phase-fast)
                  (take 101)
                  (last)
                  (map str)))
            (parse-offset "small.txt")
            (+ 8 (parse-offset "small.txt")))))

;(println offset)
;(println "Part 1:"
;         (first-8
;          (apply-multiple-phases
;           (parse-file "input.txt")
;           100)))

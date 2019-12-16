(ns dec16
  (:require [clojure.string :as string]))

(defn parse-file [f]
  (->> (string/split
        (->> (slurp f)
             (string/split-lines)
             (first)) #"")
       (map #(Integer/parseInt %))
       (vec)))

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

(defn apply-multiple-phases [numbers i]
  (if (pos? i)
    (recur (apply-phase numbers) (dec i))
    numbers))

(defn first-8 [numbers]
  (string/join
   (map str (take 8 numbers))))

(println "Part 1:"
         (first-8
          (apply-multiple-phases
           (parse-file "input.txt")
           100)))

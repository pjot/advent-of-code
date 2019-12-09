(ns dec04)
(require '[clojure.string :as string])

(defn sorted-string? [s]
  (= (sort s) s))

(defn has-duplicate? [s]
  (> 6 (count (set s))))

(defn has-two-of-something? [s]
  (contains? (set (vals (frequencies s))) 2))

(defn digit-split [n] (string/split (str n) #""))

(defn is-valid-first [n]
  (let [per-digit (digit-split n)]
    (and (sorted-string? per-digit) (has-duplicate? per-digit))))

(defn is-valid-second [n]
  (let [per-digit (digit-split n)]
    (and (sorted-string? per-digit) (has-two-of-something? per-digit))))

(defn valid-in-range [valid from to]
  (reduce + (map 
    #(if (valid %) 1 0)
    (range from to))))

(println "Part 1:" (valid-in-range is-valid-first 240920 789957))
(println "Part 2:" (valid-in-range is-valid-second 240920 789957))

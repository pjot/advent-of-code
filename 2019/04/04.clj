(ns dec04)
(require '[clojure.string :as string])

(defn sorted-string? [s]
  (= (sort s) s))

(defn has-duplicate? [s]
  (->> (set s)
       (count)
       (> 6)))

(defn has-two-of-something? [s]
  (contains?
   (->> (frequencies s)
        (vals)
        (set))
   2))

(defn digit-split [n]
  (string/split (str n) #""))

(defn is-valid-first [digits]
  (and (sorted-string? digits)
       (has-duplicate? digits)))

(defn is-valid-second [digits]
  (and (sorted-string? digits)
       (has-two-of-something? digits)))

(defn valid-in-range [valid from to]
  (->> (range from to)
       (filter #(valid (digit-split %)))
       (count)))

(println "Part 1:" (valid-in-range is-valid-first 240920 789957))
(println "Part 2:" (valid-in-range is-valid-second 240920 789957))

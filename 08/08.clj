(ns dec08)
(require '[clojure.string :as string])

(defn first-line [file]
  (string/split
   (->> (slurp file)
        (string/split-lines)
        (first)) #""))

(defn parse-file [file width height]
  (->> (first-line file)
       (map #(Integer/parseInt (str %)))
       (partition (* height width))))

(defn count-numbers [layer]
  {:ones (count (filter zero? layer))
   :count (* (count (filter (partial = 1) layer))
             (count (filter (partial = 2) layer)))})

(def layers (parse-file "image.txt" 25 6))
(println "Part 1:"
         (->> layers
              (map count-numbers)
              (sort-by :ones)
              (first)
              (:count)))
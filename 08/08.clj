(ns dec08)
(require '[clojure.string :as string])

(defn first-line [file]
  (string/split
   (->> (slurp file)
        (string/split-lines)
        (first)) #""))

(defn parse-file [file [width height]]
  (->> (first-line file)
       (map #(Integer/parseInt (str %)))
       (partition (* height width))))

(defn count-numbers [layer]
  {:ones (count (filter zero? layer))
   :count (* (count (filter (partial = 1) layer))
             (count (filter (partial = 2) layer)))})

(defn zip [a b]
  (partition 2 (interleave a b)))

(defn next-pixel [[upper lower] & _]
  (if (= upper 2) lower upper))

(defn merge-layers [upper lower]
  (map next-pixel (zip upper lower)))

(defn colorize [pixel]
  (if (= pixel 1) \u2588 " "))

(defn compose-image [layers]
  (map colorize (reduce merge-layers layers)))

(def size [25 6])

(def layers (parse-file "image.txt" size))

(println "Part 1:"
         (->> layers
              (map count-numbers)
              (sort-by :ones)
              (first)
              (:count)))

(println "Part 2:")
(println
 (->> (compose-image layers)
      (partition (first size))
      (map string/join)
      (string/join "\n")))
(ns dec10
  (:require [clojure.string :as string]))

(defn parse-row [s]
  (reduce
   (fn [row [x c]]
     (if (= c "#")
       (conj row x)
       row))
   []
   (map-indexed
    vector
    (string/split s #""))))

(defn parse-file [file]
  (reduce
   concat
   (map-indexed
    (fn [y row] (map
                 #(vector % y)
                 (parse-row row)))
    (string/split-lines (slurp file)))))

(defn calculate-angle [dx dy]
  (-> (Math/atan2 dy dx)
      (* 180)
      (/ Math/PI)
      (- 90)))

(defn round [f] (format "%.6f" f))

(defn add-to [d key val]
  (if (not (get d key))
    (assoc d key [val])
    (assoc d key
           (sort-by :distance
                    (conj (get d key) val)))))

(defn group-by-angle [[x y] asteroids]
  (reduce
   (fn [by-angle [x2 y2]]
     (let [dx (- x2 x) dy (- y y2)]
       (add-to
        by-angle
        (round (calculate-angle dx dy))
        {:x x2
         :y y2
         :distance (+ (* dx dx)
                      (* dy dy))})))
   {}
   (filter #(not= % [x y]) asteroids)))

(defn count-asteroids [coords asteroids]
  (count (group-by-angle coords asteroids)))

(defn find-station [asteroids]
  (->> asteroids
       (map #(count-asteroids % asteroids))
       (reduce max)))

(def asteroids (parse-file "input.map"))

(println "Part 1:", (find-station asteroids))
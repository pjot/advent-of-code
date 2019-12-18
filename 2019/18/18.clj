(ns dec18
  (:require [clojure.string :as string]))

(defn parse-line [y l]
  (map-indexed
    (fn [x c]
      {:x x
       :y y
       :char c})
    (string/split l #"")))

(defn point [x y] {:x x :y y})

(defn build-grid [acc p]
  (assoc acc (point (:x p) (:y p)) (:char p)))

(defn keep-robots [acc [k v]]
  (if (= v "@")
      (conj acc (point (:x k) (:y k)))
      acc))

(defn parse-file [f]
  (->> (slurp f)
       (string/split-lines)
       (map-indexed parse-line)
       (flatten)
       (seq)
       (reduce build-grid {})))

(defn neighbours [p]
  (let [x (:x p) y (:y p)]
    [(point (inc x) y)
     (point (dec x) y)
     (point x (inc y))
     (point x (dec y))]))

(defn visible-keys [grid robots keys]
  [(point 2 3) (point 5 4)])

(def grid (parse-file "small.map"))
(def robots (reduce keep-robots [] grid))
(println robots)

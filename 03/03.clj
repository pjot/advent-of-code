(ns dec03)
  (require '[clojure.string :as string])
  (require '[clojure.set :as sets])

(defn parse-int [n] (Integer/parseInt (str n)))

(defn parse-file [file]
  (->> (slurp file)
       (string/split-lines)
       (map #(string/split % #","))))

(defn direction->deltas [d]
  (case d
    \R [1 0]
    \L [-1 0]
    \U [0 1]
    \D [0 -1]))

(defn parse-direction [d]
  [(direction->deltas (first d))
   (parse-int (subs d 1))])

(defn add-coordinates [a b]
  [(+ (first a) (first b) )
   (+ (second a) (second b))])

(defn distance [[x y]] (+ (Math/abs x) (Math/abs y)))

(defn step->coordinates [coordinates [delta steps]]
  (loop [n 0
         coords coordinates
         current (add-coordinates (last coordinates) delta)]
    (if (= n steps)
      coords
      (recur (inc n)
             (conj coords current)
             (add-coordinates current delta)))))

(defn path->coordinates [path]
  (reduce step->coordinates [[0 0]] path))

(defn row->coords [r]
  (->> (map parse-direction r)
       (path->coordinates)
       (set)))

(println "Part 1:" 
  (->> (parse-file "input.path")
       (map row->coords)
       (reduce sets/intersection)
       (map distance)
       (set)
       (#(disj % 0))
       (reduce min)))
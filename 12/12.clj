(ns dec12)

(comment
(def initial-x [-1 2 4 3])
(def initial-y [0 -10 -8 5])
(def initial-z [2 -7 8 -1])
)

(def initial-x [17 1 6 19])
(def initial-y [-7 4 -2 11])
(def initial-z [-11 -1 -6 9])

(def initial-u [0 0 0 0])
(def initial-v [0 0 0 0])
(def initial-w [0 0 0 0])


(defn sum [numbers] (reduce + numbers))
(defn product [numbers] (reduce * 1 numbers))
(defn abs-sum [numbers] (reduce + (map #(Math/abs %) numbers)))

(defn zip
    ([v1 v2]
        (partition 2 (interleave v1 v2)))
    ([v1 v2 v3]
        (partition 3 (interleave v1 v2 v3))))

(defn gravity-between [a b] 
    (if (= a b) 0 
        (/ (- a b)
           (Math/abs (- a b)))))

(defn gravity-delta [points]
    (->> points
        (map (fn [p1]
            (->> points
                (map #(gravity-between % p1))
                (reduce +))))
        (vec)))

(defn multiply [v1 v2]
    (->> (zip v2 v1)
         (map product)
         (vec)))

(defn add [v1 v2]
    (->> (zip v1 v2)
         (map sum)
         (vec)))

(defn add-abs [v1 v2]
    (->> (zip v1 v2)
         (map abs-sum)
         (vec)))

(defn next-state [[positions velocities]]
    (let [new-velocities (->> positions
                              (gravity-delta)
                              (add velocities))
          new-positions (add positions new-velocities)]
        [new-positions new-velocities]))

(defn state-at [i initial-state]
    (->> initial-state
         (iterate next-state)
         (take (inc i))
         (last)))

(defn calculate-energies [[a b c]]
    (map abs-sum (zip a b c)))

(defn total-energy [positions velocities]
    (sum 
        (multiply
            (calculate-energies positions)
            (calculate-energies velocities))))

(def steps 1000)
(println
    (let [[x u] (state-at steps [initial-x initial-u])
          [y v] (state-at steps [initial-y initial-v])
          [z w] (state-at steps [initial-z initial-w])]
        (total-energy [x y z] [u v w])))
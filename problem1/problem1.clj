(defn two-sum
  "Loop through xs. Insert the complement for each x into map as {x index}.
   If the complement for a given x is found, return the index of the x and the complement."
  [xs target]
  (loop [comps {} ; map of complements and indexes
         idx 0 ; current index
         comp (- target (nth xs idx))] ; current complement
    (if (contains? comps comp)
      [(get comps comp) idx]
      (recur
       (assoc comps comp idx)
       (inc idx)
       (- target (nth xs idx))))))

(print (two-sum [2 7 11 15] 9))
; Complete the sockMerchant function below.
(defn sockMerchant [n ar]


)

(def fptr (get (System/getenv) "OUTPUT_PATH"))

(def n (Integer/parseInt (clojure.string/trim (read-line))))

(def ar (vec (map #(Integer/parseInt %) (clojure.string/split (read-line) #" "))))

(def result (sockMerchant n ar))

(spit fptr (str result "\n") :append true)

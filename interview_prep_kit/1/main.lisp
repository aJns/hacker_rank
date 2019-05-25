;; Enter your code here. Read input from STDIN. Print output to STDOUT

(progn
  (let
      ((eka-rivi (read-line))
       (toka-rivi (read-line)))
    (format t "~a~%~a~%" eka-rivi toka-rivi)))

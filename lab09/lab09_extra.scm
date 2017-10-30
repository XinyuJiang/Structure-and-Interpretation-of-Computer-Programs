;; Extra Scheme Questions ;;


; Q5
(define lst
  (cons '(1) (cons 2 (cons (cons 3 4) '(5))))
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (if (null? lst)
  	nil
  	(if (= item (car lst))
  		(remove item (cdr lst))
  		(cons (car lst) (remove item (cdr lst)))))
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (if (= 0 (min a b))
  	(max a b)
  	(if (= b 1)
  		1
  		(gcd (min a b) (modulo (max a b) (min a b)))))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  (if (null? s)
  	s
  	(cons (car s) (no-repeats (filter (lambda(x) (not (= x (car s)))) (cdr s))))
  )
)

; Q10
(define (substitute s old new)
  'YOUR-CODE-HERE
)

; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)
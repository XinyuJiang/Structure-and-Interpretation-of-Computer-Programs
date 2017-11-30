;(define (how-many-dots s)
;  (define (well-done s)
;    (cond ((null? s) True)
;      ((number? (cdr s)) False)
;      ((pair? s) (how-many-dots (cdr s))))
;    )
;    (cond ((null? s) 0)
;      ((well-done s) (+ 1 (how-many-dots (cdr s))))
;      (else (how-many-dots (cdr s)))
;    )
;)

(define (how-many-dots s)
  (if (not (pair? s)) 0
    (+ (if (not (or (pair? (cdr s))  (null? (cdr s)))) 1 0)
       (how-many-dots (car s))
       (how-many-dots (cdr s))))
)

(define (substitute s old new)
  (cond ((null? s) nil)
    ((pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)))
    ((equal? (car s) old) (cons new (substitute (cdr s) old new)))
    (else (cons (car s) (substitute (cdr s) old new)))) 
)


(define (sub-all s olds news)
  (cond ((null? s) nil)
    ((null? olds) s);do not judge car olds, judge olds directly
    (else (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))))
)

(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))


; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (make-sum 
    (derive (addend expr) var)
    (derive (augend expr) var)
  )
)

(define (derive-product expr var)
  (make-sum
    (make-product (derive (addend expr) var) (augend expr))
    (make-product (addend expr) (derive (augend expr) var))
  )
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond 
    ((=number? exponent 0) 1)
    ((=number? exponent 1) base)
    ((and (number? base) (number? exponent)) (expt base exponent))
    (else (list '^ base exponent))
  )
)

(define (base exp)
  (cadr exp)
)

(define (exponent exp)
  (caddr exp)
)

(define (exp? exp)
    (and (list? exp) (eq? (car exp) '^))
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  (make-product (augend exp) (make-exp (addend exp) (-(augend exp) 1)))
)
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s)))  
)

(define (caddr s)
  (car (cdr (cdr s))))
)

(define (sign x)
  (cond ((< x 0) -1) ((= x 0) 0) (else 1))  
)

(define (square x) (* x x))

(define (pow b n)
  (cond ((= n 1) b) ((= n 2) (square b)) ((= n 3) (* b (square b))) ((even? n) (square (pow b (/ n 2)))) 
    (else (* b (square (pow b (/ (- n 1) 2))))))
)

(define (ordered? s)
  (cond ((null? s) True) ((null? (cdr s)) True) ((> (car s) (cadr s)) False)
    (else (ordered? (cdr s))))
)

;(define (nodots s)
;  (cond ((null? s) nil) ((pair? s) (cons (car s) (nodots (cdr s))))
;    (else (cons s nil)))
;)


(define (nodots s)
  (cond ((null? s) nil) 
    ((and (pair? s) (not (or (pair? (cdr s)) (null? (cdr s))))) (list (nodots (car s)) (cdr s)))
    ((pair? s)(cons (nodots (car s)) (nodots (cdr s))))
    (else s))
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((> (car s) v) #f)
          ((= (car s) v) #t)
          (else (contains? (cdr s) v)) ; replace this line
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((> (car s) v) (cons v s)) 
          ((and (< (car s) v) (or (empty? (cdr s)) (> (cadr s) v))) (cons (car s) (cons v (cdr s))))
          ((and (< (car s) v) (cons (car s) (add (cdr s) v))))
          (else s) ; replace this line
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((> (car s) (car t)) (intersect s (cdr t)))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
          ))
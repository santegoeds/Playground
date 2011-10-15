#!/usr/bin/env csi -ss

;; Grep a single file
(define (grep-file file)
  (display (read-lines file))
  (newline))


;; Main Entry point
(define (main)
  (for-each grep-file (command-line-arguments))
  (exit))


;; Apparently this is needed for compatibility between
;; compiled Chicken and scripted execution.
(if (not (equal? (program-name) "csi"))
  (main))


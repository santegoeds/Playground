#!/usr/bin/env csi -ss

(define (main)
  (newline)
  (for-each grep-file (command-line-arguments))
  (exit))

;; Grep a single file
(define (grep-file file)
  (display file)
  (newline))

(if (not (equal? (program-name) "csi"))
  (main))


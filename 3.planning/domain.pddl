(define (domain sliding-tile)

  (:predicates
   (tile-at ?t ?r ?c)
   (is-blank ?r ?c)
   (next-row ?r1 ?r2)
   (next-column ?c1 ?c2)
  )

  (:action move-tile-down
    :parameters (?tile ?old-row ?new-row ?col)
    :precondition (and (next-row ?old-row ?new-row)
                       (tile-at ?tile ?old-row ?col)
                       (is-blank ?new-row ?col))
    :effect (and (not (tile-at ?tile ?old-row ?col))
                 (not (is-blank ?new-row ?col))
                 (tile-at ?tile ?new-row ?col)
                 (is-blank ?old-row ?col)))

  (:action move-tile-up
    :parameters (?tile ?old-row ?new-row ?col)
    :precondition (and (next-row ?new-row ?old-row)
                       (tile-at ?tile ?old-row ?col)
                       (is-blank ?new-row ?col))
    :effect (and (not (tile-at ?tile ?old-row ?col))
                 (not (is-blank ?new-row ?col))
                 (tile-at ?tile ?new-row ?col)
                 (is-blank ?old-row ?col)))

  (:action move-tile-right
    :parameters (?tile ?row ?old-col ?new-col)
    :precondition (and (next-column ?old-col ?new-col)
                       (tile-at ?tile ?row ?old-col)
                       (is-blank ?row ?new-col))
    :effect (and (not (tile-at ?tile ?row ?old-col))
                 (not (is-blank ?row ?new-col))
                 (tile-at ?tile ?row ?new-col)
                 (is-blank ?row ?old-col)))

  (:action move-tile-left
    :parameters (?tile ?row ?old-col ?new-col)
    :precondition (and (next-column ?new-col ?old-col)
                       (tile-at ?tile ?row ?old-col)
                       (is-blank ?row ?new-col))
    :effect (and (not (tile-at ?tile ?row ?old-col))
                 (not (is-blank ?row ?new-col))
                 (tile-at ?tile ?row ?new-col)
                 (is-blank ?row ?old-col)))
)

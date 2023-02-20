(define (problem eight-puzzle)
  (:domain sliding-tile)
  (:objects
     tile1 tile2 tile3 tile4 tile5
     tile6 tile7 tile8 tile9 tile10
     tile11 tile12 tile13 tile14 tile15
     tile16 tile17 tile18 tile19 tile20
     tile21 tile22 tile23 tile24
     row1 row2 row3 row4 row5
     col1 col2 col3 col4 col5)
  (:init
    (next-row row1 row2)    (next-column col1 col2)
    (next-row row2 row3)    (next-column col2 col3)
    (next-row row3 row4)    (next-column col3 col4)
    (next-row row4 row5)    (next-column col4 col5)
    
    (tile-at tile23 row1 col1)    (tile-at tile3 row1 col2)     (tile-at tile9 row1 col3)     (tile-at tile17 row1 col4)    (tile-at tile14 row1 col5)
    (tile-at tile19 row2 col1)    (tile-at tile12 row2 col2)    (tile-at tile15 row2 col3)    (tile-at tile7 row2 col4)     (tile-at tile20 row2 col5)
    (tile-at tile18 row3 col1)    (tile-at tile13 row3 col2)    (tile-at tile21 row3 col3)    (tile-at tile8 row3 col4)     (tile-at tile22 row3 col5)
    (tile-at tile6 row4 col1)     (tile-at tile10 row4 col2)    (tile-at tile2 row4 col3)     (tile-at tile11 row4 col4)    (tile-at tile1 row4 col5)
    (tile-at tile24 row5 col1)    (tile-at tile16 row5 col2)    (tile-at tile4 row5 col3)     (tile-at tile5 row5 col4)     (is-blank row5 col5))
  (:goal
   (and
    (tile-at tile1 row1 col1)     (tile-at tile2 row1 col2)     (tile-at tile3 row1 col3)     (tile-at tile4 row1 col4)     (tile-at tile5 row1 col5)
    (tile-at tile6 row2 col1)     (tile-at tile7 row2 col2)     (tile-at tile8 row2 col3)     (tile-at tile9 row2 col4)     (tile-at tile10 row2 col5)
    (tile-at tile11 row3 col1)    (tile-at tile12 row3 col2)    (tile-at tile13 row3 col3)    (tile-at tile14 row3 col4)    (tile-at tile15 row3 col5)
    (tile-at tile16 row4 col1)    (tile-at tile17 row4 col2)    (tile-at tile18 row4 col3)    (tile-at tile19 row4 col4)    (tile-at tile20 row4 col5)
    (tile-at tile21 row5 col1)    (tile-at tile22 row5 col2)    (tile-at tile23 row5 col3)    (tile-at tile24 row5 col4)    (is-blank row5 col5))))
    
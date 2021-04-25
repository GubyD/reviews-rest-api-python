sqlite> .mode csv
sqlite> .separator |
sqlite> .import --skip 1 ramen-ratings.csv reviews
sqlite> select count() from reviews;
2580
sqlite> 

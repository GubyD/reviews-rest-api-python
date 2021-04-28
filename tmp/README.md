# Database

## Open Database

    sqlite> .cd /your-directory/reviews-rest-api-python/tmp/
    sqlite> .open database.db

## Import DataSet (If required)
NOTE: **DELETE all records** in the reviews table before re-import
    
    sqlite> .mode csv
    sqlite> .separator |
    sqlite> .import --skip 1 ramen-ratings.csv reviews
    sqlite> select count() from reviews;
    2580
    sqlite> 


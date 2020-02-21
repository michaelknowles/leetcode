SELECT FirstName
    ,LastName
    ,City
    ,State
FROM Person P
LEFT OUTER JOIN Address A
    ON P.PersonID = A.PersonID;
SELECT * FROM dbo.barbora$;
SELECT * FROM dbo.delio$;
SELECT * FROM dbo.megasam24$;


-- dodawanie nowej kolumny "Jednostka_ceny" z warto�ci� 'z�'
ALTER TABLE dbo.barbora$ ADD Jednostka_ceny varchar(255);
UPDATE dbo.barbora$ SET Jednostka_ceny = 'z�';
ALTER TABLE dbo.delio$ ADD Jednostka_ceny varchar(255);
UPDATE dbo.delio$ SET Jednostka_ceny = 'z�';
ALTER TABLE dbo.megasam24$ ADD Jednostka_ceny varchar(255);
UPDATE dbo.megasam24$ SET Jednostka_ceny = 'z�';


--dodawanie nowej kolumny "Cena_za_kg" z warto�ci� produkt�w za kg
ALTER TABLE dbo.barbora$ ADD Cena_za_kg varchar(255);
UPDATE dbo.barbora$ SET Cena_za_kg = ROUND(((Cena_produktu * 1000)/Pojemno��_produktu),2);
ALTER TABLE dbo.delio$ ADD Cena_za_kg varchar(255);
UPDATE dbo.delio$ SET Cena_za_kg = ROUND(((Cena_produktu * 1000)/Pojemno��_produktu),2);
ALTER TABLE dbo.megasam24$ ADD Cena_za_kg varchar(255);
UPDATE dbo.megasam24$ SET Cena_za_kg = ROUND(((Cena_produktu* 1000)/Pojemno��_produktu),2);


--zmiana typu danych z varchar na int
ALTER TABLE dbo.barbora$ ALTER COLUMN Cena_za_kg FLOAT;
ALTER TABLE dbo.delio$ ALTER COLUMN Cena_za_kg FLOAT;
ALTER TABLE dbo.megasam24$ ALTER COLUMN Cena_za_kg FLOAT;


--ilo�� produkt�w z danej kategorii i przeci�tna cena produkt�w za kg w sklepie barbora
SELECT Typ_produktu,COUNT(*) AS 'Ilo��_produkt�w', ROUND(AVG(Cena_za_kg),2) AS '�rednia_cena produkt�w_za_kg'
FROM dbo.barbora$
GROUP BY Typ_produktu;


--ilo�� produkt�w z danej kategorii i przeci�tna cena produkt�w za kg w sklepie delio
SELECT Typ_produktu,COUNT(*) AS 'Ilo��_produkt�w', ROUND(AVG(Cena_za_kg),2) AS '�rednia_cena produkt�w_za_kg'
FROM dbo.delio$
GROUP BY Typ_produktu;


--ilo�� produkt�w z danej kategorii i przeci�tna cena produkt�w za kg w sklepie megasam24 
SELECT Typ_produktu,COUNT(*) AS 'Ilo��_produkt�w', ROUND(AVG(Cena_za_kg),2) AS '�rednia_cena produkt�w_za_kg'
FROM dbo.megasam24$
GROUP BY Typ_produktu;


--ilo�� asortymentu i przeci�tna cena produkt�w za kg we wszystkich sklepach
SELECT Sklep, COUNT(Typ_produktu) AS 'Wielko��_asortymentu', ROUND(AVG(Cena_za_kg),2) AS '�rednia_cena produkt�w_za_kg' FROM dbo.barbora$ GROUP BY Sklep
UNION ALL
SELECT Sklep, COUNT(Typ_produktu), ROUND(AVG(Cena_za_kg),2) FROM dbo.delio$ GROUP BY Sklep
UNION ALL
SELECT Sklep, COUNT(Typ_produktu), ROUND(AVG(Cena_za_kg),2) FROM dbo.megasam24$ GROUP BY Sklep;


--cena najta�szego produktu z danego rodzaju w sklepach
SELECT * FROM 
(SELECT Sklep, Typ_produktu, MIN(Cena_za_kg) AS 'Najta�szy_produkt_za_kg' FROM dbo.barbora$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MIN(Cena_za_kg) AS 'Najta�szy_produkt_za_kg' FROM dbo.delio$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MIN(Cena_za_kg) AS 'Najta�szy_produkt_za_kg' FROM dbo.megasam24$ GROUP BY Typ_produktu, Sklep) a
ORDER BY Typ_produktu ASC, Najta�szy_produkt_za_kg ASC;


--najdro�szy produkt z danego rodzaju w sklepach
SELECT * FROM 
(SELECT Sklep, Typ_produktu, MAX(Cena_za_kg) AS 'Najdro�szy_produkt_za_kg' FROM dbo.barbora$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MAX(Cena_za_kg) AS 'Najdro�szy_produkt_za_kg' FROM dbo.delio$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MAX(Cena_za_kg) AS 'Najdro�szy_produkt_za_kg' FROM dbo.megasam24$ GROUP BY Typ_produktu, Sklep) a
ORDER BY Typ_produktu DESC, Najdro�szy_produkt_za_kg DESC;


--Produkty o tej samej nazwie i pojemno�ci, kt�re wyst�puj� we wszystkich sklepach. R�nica ceny za kg pomi�dzy sklepami
SELECT dbo.delio$.Nazwa_produktu, dbo.delio$.Pojemno��_produktu, dbo.delio$.Cena_za_kg AS 'Cena_za_kg_Delio', dbo.megasam24$.Cena_za_kg AS 'Cena_za_kg_Megasam24',
dbo.barbora$.Cena_za_kg AS 'Cena_za_kg_Barbora', 
ROUND(dbo.delio$.Cena_za_kg - dbo.megasam24$.Cena_za_kg,2) AS 'R�nia_ceny_za_kg_Delio_Megasam24',
ROUND(dbo.delio$.Cena_za_kg - dbo.barbora$.Cena_za_kg,2) AS 'R�nia_ceny_za_kg_Delio_Barbora', 
ROUND(dbo.megasam24$.Cena_za_kg - dbo.delio$.Cena_za_kg,2) AS 'R�nia_ceny_za_kg_Megasam24_Delio',
ROUND(dbo.megasam24$.Cena_za_kg - dbo.barbora$.Cena_za_kg,2) AS 'R�nia_ceny_za_kg_Megasam24_Barbora',
ROUND(dbo.barbora$.Cena_za_kg - dbo.delio$.Cena_za_kg,2) AS 'R�nia_ceny_za_kg_Barbora_Delio',
ROUND(dbo.barbora$.Cena_za_kg - dbo.megasam24$.Cena_za_kg,2) AS 'R�nia_ceny_za_kg_Barbora_Megasam24'
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemno��_produktu = dbo.barbora$.Pojemno��_produktu AND dbo.delio$.Pojemno��_produktu = dbo.megasam24$.Pojemno��_produktu;


-- Najni�sza cena produktu, wyst�puj�cego w sklepach
SELECT dbo.delio$.Nazwa_produktu, dbo.delio$.Pojemno��_produktu, dbo.delio$.Cena_za_kg AS 'Cena_za_kg_Delio', dbo.megasam24$.Cena_za_kg AS 'Cena_za_kg_Megasam24',
dbo.barbora$.Cena_za_kg AS 'Cena_za_kg_Barbora',(SELECT MIN(Col) FROM (VALUES (dbo.delio$.Cena_za_kg), (dbo.megasam24$.Cena_za_kg ), (dbo.barbora$.Cena_za_kg)) AS X(Col)) AS Najni�sza_Cena
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemno��_produktu = dbo.barbora$.Pojemno��_produktu AND dbo.delio$.Pojemno��_produktu = dbo.megasam24$.Pojemno��_produktu;


-- Najwy�sza cena produktu, wyst�puj�cego w sklepach
SELECT dbo.delio$.Nazwa_produktu, dbo.delio$.Pojemno��_produktu, dbo.delio$.Cena_za_kg AS 'Cena_za_kg_Delio', dbo.megasam24$.Cena_za_kg AS 'Cena_za_kg_Megasam24',
dbo.barbora$.Cena_za_kg AS 'Cena_za_kg_Barbora',(SELECT MAX(Col) FROM (VALUES (dbo.delio$.Cena_za_kg), (dbo.megasam24$.Cena_za_kg ), (dbo.barbora$.Cena_za_kg)) AS X(Col)) AS Najni�sza_Cena
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemno��_produktu = dbo.barbora$.Pojemno��_produktu AND dbo.delio$.Pojemno��_produktu = dbo.megasam24$.Pojemno��_produktu;


--Przeci�tna cena wszystkich produkt�w, wyst�puj�cych we wszystkich sklepach
SELECT ROUND(AVG(dbo.delio$.Cena_za_kg),2) AS '�rednia_cena_za_kg_Delio',ROUND(AVG(dbo.megasam24$.Cena_za_kg),2) AS '�rednia_cena_za_kg_Megasam24', ROUND(AVG(dbo.barbora$.Cena_za_kg),2) AS '�rednia_cena_za_kg_Barbora'
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemno��_produktu = dbo.barbora$.Pojemno��_produktu AND dbo.delio$.Pojemno��_produktu = dbo.megasam24$.Pojemno��_produktu;


--Przeci�tna cena rodzaj�w produkt�w, wyst�puj�cych we wszystkich sklepach
SELECT dbo.delio$.Typ_produktu,ROUND(AVG(dbo.delio$.Cena_za_kg),2) AS '�rednia_cena_za_kg_Delio',ROUND(AVG(dbo.megasam24$.Cena_za_kg),2) AS '�rednia_cena_za_kg_Megasam24', ROUND(AVG(dbo.barbora$.Cena_za_kg),2) AS '�rednia_cena_za_kg_Barbora'
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemno��_produktu = dbo.barbora$.Pojemno��_produktu AND dbo.delio$.Pojemno��_produktu = dbo.megasam24$.Pojemno��_produktu
GROUP BY dbo.delio$.Typ_produktu;

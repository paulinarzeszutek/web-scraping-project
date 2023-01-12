SELECT * FROM dbo.barbora$;
SELECT * FROM dbo.delio$;
SELECT * FROM dbo.megasam24$;


-- dodawanie nowej kolumny "Jednostka_ceny" z wartoœci¹ 'z³'
ALTER TABLE dbo.barbora$ ADD Jednostka_ceny varchar(255);
UPDATE dbo.barbora$ SET Jednostka_ceny = 'z³';
ALTER TABLE dbo.delio$ ADD Jednostka_ceny varchar(255);
UPDATE dbo.delio$ SET Jednostka_ceny = 'z³';
ALTER TABLE dbo.megasam24$ ADD Jednostka_ceny varchar(255);
UPDATE dbo.megasam24$ SET Jednostka_ceny = 'z³';


--dodawanie nowej kolumny "Cena_za_kg" z wartoœci¹ produktów za kg
ALTER TABLE dbo.barbora$ ADD Cena_za_kg varchar(255);
UPDATE dbo.barbora$ SET Cena_za_kg = ROUND(((Cena_produktu * 1000)/Pojemnoœæ_produktu),2);
ALTER TABLE dbo.delio$ ADD Cena_za_kg varchar(255);
UPDATE dbo.delio$ SET Cena_za_kg = ROUND(((Cena_produktu * 1000)/Pojemnoœæ_produktu),2);
ALTER TABLE dbo.megasam24$ ADD Cena_za_kg varchar(255);
UPDATE dbo.megasam24$ SET Cena_za_kg = ROUND(((Cena_produktu* 1000)/Pojemnoœæ_produktu),2);


--zmiana typu danych z varchar na int
ALTER TABLE dbo.barbora$ ALTER COLUMN Cena_za_kg FLOAT;
ALTER TABLE dbo.delio$ ALTER COLUMN Cena_za_kg FLOAT;
ALTER TABLE dbo.megasam24$ ALTER COLUMN Cena_za_kg FLOAT;


--iloœæ produktów z danej kategorii i przeciêtna cena produktów za kg w sklepie barbora
SELECT Typ_produktu,COUNT(*) AS 'Iloœæ_produktów', ROUND(AVG(Cena_za_kg),2) AS 'Œrednia_cena produktów_za_kg'
FROM dbo.barbora$
GROUP BY Typ_produktu;


--iloœæ produktów z danej kategorii i przeciêtna cena produktów za kg w sklepie delio
SELECT Typ_produktu,COUNT(*) AS 'Iloœæ_produktów', ROUND(AVG(Cena_za_kg),2) AS 'Œrednia_cena produktów_za_kg'
FROM dbo.delio$
GROUP BY Typ_produktu;


--iloœæ produktów z danej kategorii i przeciêtna cena produktów za kg w sklepie megasam24 
SELECT Typ_produktu,COUNT(*) AS 'Iloœæ_produktów', ROUND(AVG(Cena_za_kg),2) AS 'Œrednia_cena produktów_za_kg'
FROM dbo.megasam24$
GROUP BY Typ_produktu;


--iloœæ asortymentu i przeciêtna cena produktów za kg we wszystkich sklepach
SELECT Sklep, COUNT(Typ_produktu) AS 'Wielkoœæ_asortymentu', ROUND(AVG(Cena_za_kg),2) AS 'Œrednia_cena produktów_za_kg' FROM dbo.barbora$ GROUP BY Sklep
UNION ALL
SELECT Sklep, COUNT(Typ_produktu), ROUND(AVG(Cena_za_kg),2) FROM dbo.delio$ GROUP BY Sklep
UNION ALL
SELECT Sklep, COUNT(Typ_produktu), ROUND(AVG(Cena_za_kg),2) FROM dbo.megasam24$ GROUP BY Sklep;


--cena najtañszego produktu z danego rodzaju w sklepach
SELECT * FROM 
(SELECT Sklep, Typ_produktu, MIN(Cena_za_kg) AS 'Najtañszy_produkt_za_kg' FROM dbo.barbora$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MIN(Cena_za_kg) AS 'Najtañszy_produkt_za_kg' FROM dbo.delio$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MIN(Cena_za_kg) AS 'Najtañszy_produkt_za_kg' FROM dbo.megasam24$ GROUP BY Typ_produktu, Sklep) a
ORDER BY Typ_produktu ASC, Najtañszy_produkt_za_kg ASC;


--najdro¿szy produkt z danego rodzaju w sklepach
SELECT * FROM 
(SELECT Sklep, Typ_produktu, MAX(Cena_za_kg) AS 'Najdro¿szy_produkt_za_kg' FROM dbo.barbora$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MAX(Cena_za_kg) AS 'Najdro¿szy_produkt_za_kg' FROM dbo.delio$ GROUP BY Typ_produktu, Sklep
UNION ALL
SELECT Sklep, Typ_produktu, MAX(Cena_za_kg) AS 'Najdro¿szy_produkt_za_kg' FROM dbo.megasam24$ GROUP BY Typ_produktu, Sklep) a
ORDER BY Typ_produktu DESC, Najdro¿szy_produkt_za_kg DESC;


--Produkty o tej samej nazwie i pojemnoœci, które wystêpuj¹ we wszystkich sklepach. Ró¿nica ceny za kg pomiêdzy sklepami
SELECT dbo.delio$.Nazwa_produktu, dbo.delio$.Pojemnoœæ_produktu, dbo.delio$.Cena_za_kg AS 'Cena_za_kg_Delio', dbo.megasam24$.Cena_za_kg AS 'Cena_za_kg_Megasam24',
dbo.barbora$.Cena_za_kg AS 'Cena_za_kg_Barbora', 
ROUND(dbo.delio$.Cena_za_kg - dbo.megasam24$.Cena_za_kg,2) AS 'Ró¿nia_ceny_za_kg_Delio_Megasam24',
ROUND(dbo.delio$.Cena_za_kg - dbo.barbora$.Cena_za_kg,2) AS 'Ró¿nia_ceny_za_kg_Delio_Barbora', 
ROUND(dbo.megasam24$.Cena_za_kg - dbo.delio$.Cena_za_kg,2) AS 'Ró¿nia_ceny_za_kg_Megasam24_Delio',
ROUND(dbo.megasam24$.Cena_za_kg - dbo.barbora$.Cena_za_kg,2) AS 'Ró¿nia_ceny_za_kg_Megasam24_Barbora',
ROUND(dbo.barbora$.Cena_za_kg - dbo.delio$.Cena_za_kg,2) AS 'Ró¿nia_ceny_za_kg_Barbora_Delio',
ROUND(dbo.barbora$.Cena_za_kg - dbo.megasam24$.Cena_za_kg,2) AS 'Ró¿nia_ceny_za_kg_Barbora_Megasam24'
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemnoœæ_produktu = dbo.barbora$.Pojemnoœæ_produktu AND dbo.delio$.Pojemnoœæ_produktu = dbo.megasam24$.Pojemnoœæ_produktu;


-- Najni¿sza cena produktu, wystêpuj¹cego w sklepach
SELECT dbo.delio$.Nazwa_produktu, dbo.delio$.Pojemnoœæ_produktu, dbo.delio$.Cena_za_kg AS 'Cena_za_kg_Delio', dbo.megasam24$.Cena_za_kg AS 'Cena_za_kg_Megasam24',
dbo.barbora$.Cena_za_kg AS 'Cena_za_kg_Barbora',(SELECT MIN(Col) FROM (VALUES (dbo.delio$.Cena_za_kg), (dbo.megasam24$.Cena_za_kg ), (dbo.barbora$.Cena_za_kg)) AS X(Col)) AS Najni¿sza_Cena
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemnoœæ_produktu = dbo.barbora$.Pojemnoœæ_produktu AND dbo.delio$.Pojemnoœæ_produktu = dbo.megasam24$.Pojemnoœæ_produktu;


-- Najwy¿sza cena produktu, wystêpuj¹cego w sklepach
SELECT dbo.delio$.Nazwa_produktu, dbo.delio$.Pojemnoœæ_produktu, dbo.delio$.Cena_za_kg AS 'Cena_za_kg_Delio', dbo.megasam24$.Cena_za_kg AS 'Cena_za_kg_Megasam24',
dbo.barbora$.Cena_za_kg AS 'Cena_za_kg_Barbora',(SELECT MAX(Col) FROM (VALUES (dbo.delio$.Cena_za_kg), (dbo.megasam24$.Cena_za_kg ), (dbo.barbora$.Cena_za_kg)) AS X(Col)) AS Najni¿sza_Cena
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemnoœæ_produktu = dbo.barbora$.Pojemnoœæ_produktu AND dbo.delio$.Pojemnoœæ_produktu = dbo.megasam24$.Pojemnoœæ_produktu;


--Przeciêtna cena wszystkich produktów, wystêpuj¹cych we wszystkich sklepach
SELECT ROUND(AVG(dbo.delio$.Cena_za_kg),2) AS 'Œrednia_cena_za_kg_Delio',ROUND(AVG(dbo.megasam24$.Cena_za_kg),2) AS 'Œrednia_cena_za_kg_Megasam24', ROUND(AVG(dbo.barbora$.Cena_za_kg),2) AS 'Œrednia_cena_za_kg_Barbora'
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemnoœæ_produktu = dbo.barbora$.Pojemnoœæ_produktu AND dbo.delio$.Pojemnoœæ_produktu = dbo.megasam24$.Pojemnoœæ_produktu;


--Przeciêtna cena rodzajów produktów, wystêpuj¹cych we wszystkich sklepach
SELECT dbo.delio$.Typ_produktu,ROUND(AVG(dbo.delio$.Cena_za_kg),2) AS 'Œrednia_cena_za_kg_Delio',ROUND(AVG(dbo.megasam24$.Cena_za_kg),2) AS 'Œrednia_cena_za_kg_Megasam24', ROUND(AVG(dbo.barbora$.Cena_za_kg),2) AS 'Œrednia_cena_za_kg_Barbora'
FROM (dbo.delio$
INNER JOIN dbo.megasam24$ ON dbo.delio$.Nazwa_produktu = dbo.megasam24$.Nazwa_produktu
INNER JOIN dbo.barbora$ ON dbo.delio$.Nazwa_produktu = dbo.barbora$.Nazwa_produktu)
WHERE dbo.delio$.Pojemnoœæ_produktu = dbo.barbora$.Pojemnoœæ_produktu AND dbo.delio$.Pojemnoœæ_produktu = dbo.megasam24$.Pojemnoœæ_produktu
GROUP BY dbo.delio$.Typ_produktu;

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Sélection de la base de données hbnb_dev_db pour effectuer les opérations suivantes
USE hbnb_dev_db;

-- Crée la table 'users' avec les colonnes 'username', 'password', 'email', 'first_name' et 'last_name'
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255), -- Ajoute la colonne 'first_name'
    last_name VARCHAR(255) -- Ajoute la colonne 'last_name'
);

-- Flush privileges pour appliquer les modifications
FLUSH PRIVILEGES;


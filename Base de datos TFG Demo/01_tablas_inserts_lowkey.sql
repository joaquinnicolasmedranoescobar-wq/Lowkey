CREATE DATABASE lowkey_db;
USE lowkey_db;

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('ACTIVO','INACTIVO') DEFAULT 'ACTIVO'
);

CREATE TABLE tipos_combustible (
    id_combustible INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE vehiculos (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    matricula VARCHAR(20) UNIQUE NOT NULL,
    marca VARCHAR(80) NOT NULL,
    modelo VARCHAR(80) NOT NULL,
    kilometraje INT NOT NULL,
    id_combustible INT NOT NULL,
    observaciones TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('ACTIVO','INACTIVO') DEFAULT 'ACTIVO',

    FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario),

    FOREIGN KEY (id_combustible)
        REFERENCES tipos_combustible(id_combustible)
);

CREATE TABLE tipos_mantenimiento (
    id_tipo_mantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE mantenimientos (
    id_mantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo INT NOT NULL,
    id_tipo_mantenimiento INT NOT NULL,
    fecha DATE NOT NULL,
    kilometros INT NOT NULL,
    costo DECIMAL(10,2) NOT NULL,
    descripcion TEXT,

    FOREIGN KEY (id_vehiculo)
        REFERENCES vehiculos(id_vehiculo),

    FOREIGN KEY (id_tipo_mantenimiento)
        REFERENCES tipos_mantenimiento(id_tipo_mantenimiento)
);

CREATE TABLE categorias_gastos (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE gastos (
    id_gasto INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo INT NOT NULL,
    id_categoria INT NOT NULL,
    fecha DATE NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    descripcion TEXT,

    FOREIGN KEY (id_vehiculo)
        REFERENCES vehiculos(id_vehiculo),

    FOREIGN KEY (id_categoria)
        REFERENCES categorias_gastos(id_categoria)
);

CREATE TABLE estadisticas_mensuales (
    id_estadistica INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo INT NOT NULL,
    mes INT NOT NULL,
    anio INT NOT NULL,
    gasto_total DECIMAL(10,2),
    mantenimientos_totales INT,

    FOREIGN KEY (id_vehiculo)
        REFERENCES vehiculos(id_vehiculo)
);

INSERT INTO tipos_combustible(nombre)
VALUES
('Gasolina'),
('Diésel'),
('Híbrido'),
('Eléctrico');

INSERT INTO tipos_mantenimiento(nombre)
VALUES
('Cambio de aceite'),
('Neumáticos'),
('Frenos'),
('ITV'),
('Revisión general');

INSERT INTO categorias_gastos(nombre)
VALUES
('Mantenimiento'),
('Combustible'),
('ITV y tasas'),
('Seguro'),
('Lavado');

INSERT INTO usuarios(nombre,email,password_hash)
VALUES
('Carlos Ruiz','carlos@gmail.com','123456'),
('Ana Torres','ana@gmail.com','123456');

INSERT INTO vehiculos
(id_usuario,nombre,matricula,marca,modelo,kilometraje,id_combustible,observaciones)
VALUES
(1,'Golf Azul','1234ABC','Volkswagen','Golf',154000,1,'Vehículo principal'),
(2,'Seat León','5678DEF','Seat','León',98000,2,'Uso diario');

INSERT INTO mantenimientos
(id_vehiculo,id_tipo_mantenimiento,fecha,kilometros,costo,descripcion)
VALUES
(1,1,'2026-05-01',154200,82.00,'Cambio de aceite completo'),
(1,2,'2026-04-10',151900,260.00,'Cambio neumáticos delanteros'),
(2,5,'2026-05-03',98000,150.00,'Revisión general');

INSERT INTO gastos
(id_vehiculo,id_categoria,fecha,monto,descripcion)
VALUES
(1,2,'2026-05-02',72.00,'Combustible semanal'),
(1,1,'2026-05-01',156.00,'Mantenimiento mensual'),
(2,4,'2026-05-04',320.00,'Seguro anual');


DELIMITER //

CREATE PROCEDURE sp_registrar_usuario(
    IN p_nombre VARCHAR(100),
    IN p_email VARCHAR(120),
    IN p_password VARCHAR(255)
)
BEGIN
    INSERT INTO usuarios(nombre,email,password_hash)
    VALUES(p_nombre,p_email,p_password);
END //

CREATE PROCEDURE sp_registrar_vehiculo(
    IN p_id_usuario INT,
    IN p_nombre VARCHAR(100),
    IN p_matricula VARCHAR(20),
    IN p_marca VARCHAR(80),
    IN p_modelo VARCHAR(80),
    IN p_km INT,
    IN p_combustible INT,
    IN p_obs TEXT
)
BEGIN
    INSERT INTO vehiculos
    (id_usuario,nombre,matricula,marca,modelo,kilometraje,id_combustible,observaciones)
    VALUES
    (p_id_usuario,p_nombre,p_matricula,p_marca,p_modelo,p_km,p_combustible,p_obs);
END //

CREATE PROCEDURE sp_registrar_mantenimiento(
    IN p_id_vehiculo INT,
    IN p_tipo INT,
    IN p_fecha DATE,
    IN p_km INT,
    IN p_costo DECIMAL(10,2),
    IN p_descripcion TEXT
)
BEGIN
    INSERT INTO mantenimientos
    (id_vehiculo,id_tipo_mantenimiento,fecha,kilometros,costo,descripcion)
    VALUES
    (p_id_vehiculo,p_tipo,p_fecha,p_km,p_costo,p_descripcion);
END //

CREATE PROCEDURE sp_registrar_gasto(
    IN p_id_vehiculo INT,
    IN p_categoria INT,
    IN p_fecha DATE,
    IN p_monto DECIMAL(10,2),
    IN p_descripcion TEXT
)
BEGIN
    INSERT INTO gastos
    (id_vehiculo,id_categoria,fecha,monto,descripcion)
    VALUES
    (p_id_vehiculo,p_categoria,p_fecha,p_monto,p_descripcion);
END //

CREATE PROCEDURE sp_obtener_vehiculos_usuario(
    IN p_id_usuario INT
)
BEGIN
    SELECT *
    FROM vehiculos
    WHERE id_usuario = p_id_usuario;
END //

CREATE PROCEDURE sp_historial_mantenimientos(
    IN p_id_vehiculo INT
)
BEGIN
    SELECT m.*, tm.nombre AS tipo
    FROM mantenimientos m
    INNER JOIN tipos_mantenimiento tm
    ON m.id_tipo_mantenimiento = tm.id_tipo_mantenimiento
    WHERE m.id_vehiculo = p_id_vehiculo
    ORDER BY fecha DESC;
END //

CREATE PROCEDURE sp_total_gastos_vehiculo(
    IN p_id_vehiculo INT
)
BEGIN
    SELECT SUM(monto) AS total_gastos
    FROM gastos
    WHERE id_vehiculo = p_id_vehiculo;
END //

CREATE PROCEDURE sp_actualizar_kilometraje(
    IN p_id_vehiculo INT,
    IN p_km INT
)
BEGIN
    UPDATE vehiculos
    SET kilometraje = p_km
    WHERE id_vehiculo = p_id_vehiculo;
END //

CREATE PROCEDURE sp_eliminar_vehiculo(
    IN p_id_vehiculo INT
)
BEGIN
    DELETE FROM vehiculos
    WHERE id_vehiculo = p_id_vehiculo;
END //

CREATE PROCEDURE sp_estadisticas_mensuales(
    IN p_mes INT,
    IN p_anio INT
)
BEGIN
    SELECT
        v.nombre,
        SUM(g.monto) AS total_gastos,
        COUNT(m.id_mantenimiento) AS total_mantenimientos
    FROM vehiculos v
    LEFT JOIN gastos g
        ON v.id_vehiculo = g.id_vehiculo
    LEFT JOIN mantenimientos m
        ON v.id_vehiculo = m.id_vehiculo
    WHERE MONTH(g.fecha) = p_mes
    AND YEAR(g.fecha) = p_anio
    GROUP BY v.nombre;
END //

DELIMITER ;




VISTAS


CREATE VIEW vw_resumen_vehiculos AS
SELECT
    v.id_vehiculo,
    v.nombre,
    v.matricula,
    v.marca,
    v.modelo,
    tc.nombre AS combustible,
    v.kilometraje
FROM vehiculos v
INNER JOIN tipos_combustible tc
ON v.id_combustible = tc.id_combustible;

CREATE VIEW vw_gastos_totales AS
SELECT
    v.nombre AS vehiculo,
    SUM(g.monto) AS total_gastado
FROM vehiculos v
INNER JOIN gastos g
ON v.id_vehiculo = g.id_vehiculo
GROUP BY v.nombre;


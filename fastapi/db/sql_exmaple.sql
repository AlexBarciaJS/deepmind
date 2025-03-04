-- Crear la base de datos
CREATE DATABASE empresa_db;
USE empresa_db;

-- Crear tabla de departamentos
CREATE TABLE departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Crear tabla de empleados
CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    salario DECIMAL(10,2),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id) ON DELETE SET NULL
);

-- Crear tabla de proyectos
CREATE TABLE proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    presupuesto DECIMAL(12,2),
    lider_id INT,
    FOREIGN KEY (lider_id) REFERENCES empleados(id) ON DELETE SET NULL
);

-- Tabla intermedia empleados_proyectos (relación muchos a muchos)
CREATE TABLE empleados_proyectos (
    empleado_id INT,
    proyecto_id INT,
    PRIMARY KEY (empleado_id, proyecto_id),
    FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
    FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
);

-- Crear tabla de clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Crear tabla de facturas
CREATE TABLE facturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    fecha DATE NOT NULL,
    total DECIMAL(12,2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

-- Crear tabla de proveedores
CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

-- Crear tabla de productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    proveedor_id INT,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores(id) ON DELETE SET NULL
);

-- Tabla intermedia facturas_productos (relación muchos a muchos)
CREATE TABLE facturas_productos (
    factura_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    PRIMARY KEY (factura_id, producto_id),
    FOREIGN KEY (factura_id) REFERENCES facturas(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
);

-- Insertar datos en departamentos
INSERT INTO departamentos (nombre) VALUES
('Recursos Humanos'),
('IT'),
('Ventas'),
('Marketing'),
('Finanzas');

-- Insertar datos en empleados
INSERT INTO empleados (nombre, email, salario, departamento_id) VALUES
('Juan Pérez', 'juan@example.com', 3000, 1),
('Ana Gómez', 'ana@example.com', 3500, 2),
('Carlos López', 'carlos@example.com', 4000, 3),
('Laura Martínez', 'laura@example.com', 3200, 4),
('Miguel Torres', 'miguel@example.com', 2800, 5),
('Lucía Fernández', 'lucia@example.com', 3700, 1),
('Roberto Díaz', 'roberto@example.com', 3600, 2),
('Sofía Ramírez', 'sofia@example.com', 3300, 3),
('Alejandro Castro', 'alejandro@example.com', 3100, 4),
('María Ríos', 'maria@example.com', 2900, 5);

-- Insertar datos en proyectos
INSERT INTO proyectos (nombre, presupuesto, lider_id) VALUES
('Proyecto A', 50000, 1),
('Proyecto B', 75000, 2),
('Proyecto C', 100000, 3);

-- Insertar relaciones en empleados_proyectos
INSERT INTO empleados_proyectos (empleado_id, proyecto_id) VALUES
(1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 1), (8, 2), (9, 3), (10, 1);

-- Insertar datos en clientes
INSERT INTO clientes (nombre, email) VALUES
('Empresa X', 'contacto@empresa-x.com'),
('Empresa Y', 'contacto@empresa-y.com'),
('Empresa Z', 'contacto@empresa-z.com'),
('Cliente 1', 'cliente1@example.com'),
('Cliente 2', 'cliente2@example.com'),
('Cliente 3', 'cliente3@example.com'),
('Cliente 4', 'cliente4@example.com'),
('Cliente 5', 'cliente5@example.com'),
('Cliente 6', 'cliente6@example.com'),
('Cliente 7', 'cliente7@example.com');

-- Insertar datos en facturas
INSERT INTO facturas (cliente_id, fecha, total) VALUES
(1, '2024-03-01', 1500),
(2, '2024-03-02', 2500),
(3, '2024-03-03', 1800),
(4, '2024-03-04', 1200),
(5, '2024-03-05', 2200),
(6, '2024-03-06', 3000),
(7, '2024-03-07', 2750),
(8, '2024-03-08', 2100),
(9, '2024-03-09', 1950),
(10, '2024-03-10', 3100);

-- Insertar datos en proveedores
INSERT INTO proveedores (nombre, telefono) VALUES
('Proveedor A', '123456789'),
('Proveedor B', '987654321'),
('Proveedor C', '456123789'),
('Proveedor D', '789654123');

-- Insertar datos en productos
INSERT INTO productos (nombre, precio, proveedor_id) VALUES
('Producto 1', 50, 1),
('Producto 2', 75, 1),
('Producto 3', 30, 2),
('Producto 4', 120, 2),
('Producto 5', 200, 3),
('Producto 6', 90, 3),
('Producto 7', 40, 4),
('Producto 8', 80, 4),
('Producto 9', 150, 1),
('Producto 10', 60, 2);

-- Insertar datos en facturas_productos
INSERT INTO facturas_productos (factura_id, producto_id, cantidad) VALUES
(1, 1, 2), (2, 2, 3), (3, 3, 1), (4, 4, 4), (5, 5, 2), 
(6, 6, 1), (7, 7, 5), (8, 8, 2), (9, 9, 3), (10, 10, 4);

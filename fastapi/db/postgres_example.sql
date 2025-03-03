
-- Crear tabla de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);

-- Crear tabla de pedidos
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
    producto_id INT REFERENCES productos(id) ON DELETE CASCADE,
    cantidad INT NOT NULL,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos en usuarios
INSERT INTO usuarios (nombre, email) VALUES
('Juan Pérez', 'juan@example.com'),
('María López', 'maria@example.com'),
('Carlos Sánchez', 'carlos@example.com');

-- Insertar datos en productos
INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop', 1200.50, 10),
('Mouse', 25.99, 50),
('Teclado', 45.75, 30);

-- Insertar datos en pedidos
INSERT INTO pedidos (usuario_id, producto_id, cantidad) VALUES
(1, 1, 1), -- Juan compró una Laptop
(2, 2, 2), -- María compró 2 Mouse
(3, 3, 1), -- Carlos compró un Teclado
(1, 2, 1), -- Juan compró un Mouse
(2, 1, 1); -- María compró una Laptop

-- Consultas de ejemplo para LangChain
-- Obtener todos los pedidos con información de usuario y producto
SELECT 
    p.id AS pedido_id, 
    u.nombre AS usuario, 
    pr.nombre AS producto, 
    p.cantidad, 
    p.fecha_pedido
FROM pedidos p
JOIN usuarios u ON p.usuario_id = u.id
JOIN productos pr ON p.producto_id = pr.id;

-- Obtener total gastado por cada usuario
SELECT 
    u.nombre AS usuario, 
    SUM(pr.precio * p.cantidad) AS total_gastado
FROM pedidos p
JOIN usuarios u ON p.usuario_id = u.id
JOIN productos pr ON p.producto_id = pr.id
GROUP BY u.nombre
ORDER BY total_gastado DESC;

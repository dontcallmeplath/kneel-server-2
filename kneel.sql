-- Run this block if you already have a database and need to re-create it
DELETE FROM Metal;
DELETE FROM Style;
DELETE FROM Size;

DROP TABLE IF EXISTS Metal;
DROP TABLE IF EXISTS Style;
DROP TABLE IF EXISTS Size;
DROP TABLE IF EXISTS `Order`;
-- End block


-- Run this block to create the tables and seed them with some initial data
CREATE TABLE `Metal` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Style` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE `Size` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `caret` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Order` (
    `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `metal_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)
);



INSERT INTO `Metal` VALUES (null, 'Silver', 500);
INSERT INTO `Metal` VALUES (null, 'Gold', 1000);
INSERT INTO `Metal` VALUES (null, 'Rose Gold', 750);
INSERT INTO `Metal` VALUES (null, 'Platinum', 1500);
INSERT INTO `Metal` VALUES (null, 'Tungsten', 2000);

INSERT INTO `Style` VALUES (null, 'Princess', 2500);
INSERT INTO `Style` VALUES (null, 'Original', 1000);
INSERT INTO `Style` VALUES (null, 'Oval', 1500);
INSERT INTO `Style` VALUES (null, 'Heart', 1750);
INSERT INTO `Style` VALUES (null, 'Round', 2000);

INSERT INTO `Size` VALUES (null, 10, 400);
INSERT INTO `Size` VALUES (null, 12, 500);
INSERT INTO `Size` VALUES (null, 18, 800);
INSERT INTO `Size` VALUES (null, 24, 1000);
INSERT INTO `Size` VALUES (null, 32, 1500);

INSERT INTO `Order`(metal_id, style_id, size_id) VALUES (2, 3, 5);
INSERT INTO `Order`(metal_id, style_id, size_id) VALUES (1, 5, 4);
INSERT INTO `Order`(metal_id, style_id, size_id) VALUES (5, 1, 3);
INSERT INTO `Order`(metal_id, style_id, size_id) VALUES (4, 2, 2);
INSERT INTO `Order`(metal_id, style_id, size_id) VALUES (3, 4, 1);

SELECT o.id, o.metal_id, o.style_id, o.size_id, m.id, m.metal, m.price FROM `Order` o JOIN Metal m ON o.metal_id = m.id WHERE m.id = 5;
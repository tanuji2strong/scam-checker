CREATE TABLE checks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    checked_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    message TEXT NOT NULL,
    risk ENUM('low','medium','high') NOT NULL,
    scam_type VARCHAR(30) NOT NULL,
    red_flags JSON NOT NULL,
    judge ENUM('llm','keyword') NOT NULL
);
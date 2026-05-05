-- ============================================
-- 从 PostgreSQL JSON 导出迁移到 MySQL
-- 用法：在 MySQL 客户端中执行此文件
--   mysql -u root -p < schema.sql
-- ============================================

CREATE DATABASE IF NOT EXISTS my_study_data
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE my_study_data;

-- 用户表
CREATE TABLE users (
    id            INT          NOT NULL PRIMARY KEY,
    username      VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role          VARCHAR(20)  NOT NULL DEFAULT 'user',
    display_name  VARCHAR(100) DEFAULT NULL,
    email         VARCHAR(255) DEFAULT NULL,
    is_active     TINYINT(1)   NOT NULL DEFAULT 1,
    created_at    DATETIME(6)  NOT NULL,
    updated_at    DATETIME(6)  NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 设备表
CREATE TABLE devices (
    id          INT          NOT NULL PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    device_type VARCHAR(50)  NOT NULL,
    device_sn   VARCHAR(100) NOT NULL UNIQUE,
    mqtt_topic  VARCHAR(255) DEFAULT NULL,
    location    VARCHAR(255) DEFAULT NULL,
    status      JSON         DEFAULT NULL,
    is_online   TINYINT(1)   NOT NULL DEFAULT 0,
    last_seen   DATETIME(6)  DEFAULT NULL,
    created_at  DATETIME(6)  NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 文档表
CREATE TABLE documents (
    id             INT          NOT NULL PRIMARY KEY,
    title          VARCHAR(255) NOT NULL,
    description    TEXT         DEFAULT NULL,
    file_key       VARCHAR(500) DEFAULT NULL,
    file_name      VARCHAR(255) DEFAULT NULL,
    file_size      INT          DEFAULT NULL,
    file_type      VARCHAR(50)  DEFAULT NULL,
    uploaded_by    INT          DEFAULT NULL,
    download_count INT          NOT NULL DEFAULT 0,
    created_at     DATETIME(6)  NOT NULL,
    updated_at     DATETIME(6)  NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 学习记录表
CREATE TABLE study_records (
    id         INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id    INT          DEFAULT NULL,
    title      VARCHAR(255) DEFAULT NULL,
    content    TEXT         DEFAULT NULL,
    created_at DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 设备状态日志表
CREATE TABLE device_status_logs (
    id          BIGINT       NOT NULL PRIMARY KEY,
    device_id   INT          NOT NULL,
    payload     JSON         DEFAULT NULL,
    recorded_at DATETIME(6)  NOT NULL,
    INDEX idx_device_id (device_id),
    INDEX idx_recorded_at (recorded_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

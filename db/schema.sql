PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS import_log (
    id INTEGER PRIMARY KEY,
    source_path TEXT NOT NULL,
    source_hash TEXT NOT NULL,
    sheet_name TEXT,
    target_table TEXT NOT NULL,
    row_count INTEGER NOT NULL DEFAULT 0,
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (source_hash, sheet_name)
);

CREATE INDEX IF NOT EXISTS idx_import_log_source_path ON import_log (source_path);

import aiosqlite
import loguru
from typing import List, Dict
from app.config import db_path



async def sql_execute(sql: str):
    async with aiosqlite.connect(db_path) as db:
        try:
            await db.execute('BEGIN')
            await db.execute(sql)
            await db.execute('COMMIT')
        except aiosqlite.Error as e:
            await db.execute('ROLLBACK')
            loguru.logger.error(f"Error executing SQL statement '{sql}'")
            loguru.logger.exception(e)
            raise


async def sql_execute_many(sql: str, args: List[List]):
    async with aiosqlite.connect(db_path) as db:
        try:
            await db.executemany(sql, args)
            await db.commit()
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e


async def sql_executescript(sql: str) -> None:
    async with aiosqlite.connect(db_path) as db:
        try:
            await db.executescript(sql)
            await db.commit()
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e


async def sql_fetchone(sql: str) -> list:
    async with aiosqlite.connect(db_path) as db:
        try:
            cur = await db.execute(sql)
            res = await cur.fetchone()
            return res
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e


async def sql_fetchall(sql: str) -> list:
    async with aiosqlite.connect(db_path) as db:
        try:
            cur = await db.execute(sql)
            res = await cur.fetchall()
            return res
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e


async def sql_execute_safe(sql: str, args: list):
    async with aiosqlite.connect(db_path) as db:
        try:
            await db.execute(sql, args)
            await db.commit()
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e


async def sql_fetchone_safe(sql: str, args: list):
    async with aiosqlite.connect(db_path) as db:
        try:
            cur = await db.execute(sql, args)
            res = await cur.fetchone()
            return res
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e


async def sql_fetchone_col_name(sql: str) -> Dict or None:
    async with aiosqlite.connect(db_path) as db:
        try:
            cur = await db.execute(sql)
            res = await cur.fetchone()
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e
    if not res:
        return None
    if res:
        columns = [col[0] for col in cur.description]
        return dict(zip(columns, res))


async def sql_fetchall_col_name(sql: str) -> List[Dict] or None:
    async with aiosqlite.connect(db_path) as db:
        try:
            cur = await db.execute(sql)
            res = await cur.fetchall()
        except Exception as e:
            loguru.logger.error(f'Error executing SQL statement "{sql}"')
            loguru.logger.exception(e)
            raise e
    if not res:
        return None
    if res:
        columns = [col[0] for col in cur.description]
        return [dict(zip(columns, i)) for i in res]


from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Глобальный словарь для хранения задач пользователей
user_tasks = {}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я твой помощник по задачам. Используй /add чтобы добавить задачу, /remove чтобы удалить задачу и /list чтобы посмотреть список задач.')

# Команда /add
async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    task = ' '.join(context.args)
    if user_id not in user_tasks:
        user_tasks[user_id] = []
    user_tasks[user_id].append(task)
    await update.message.reply_text(f'Задача "{task}" добавлена.')

# Команда /remove
async def remove_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if user_id in user_tasks and user_tasks[user_id]:
        task = user_tasks[user_id].pop()
        await update.message.reply_text(f'Задача "{task}" удалена.')
    else:
        await update.message.reply_text('Нет задач для удаления.')

# Команда /list
async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if user_id in user_tasks and user_tasks[user_id]:
        tasks = "\n".join(user_tasks[user_id])
        await update.message.reply_text(f'Твои задачи:\n{tasks}')
    else:
        await update.message.reply_text('Твой список задач пуст.')

def main() -> None:
    # Вставьте сюда ваш токен
    application = Application.builder().token("твой токен").build()

    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("remove", remove_task))
    application.add_handler(CommandHandler("list", list_tasks))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
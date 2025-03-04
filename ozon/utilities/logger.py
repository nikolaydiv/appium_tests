import datetime
import os

class Logger():
    logs_folder = os.path.join(os.path.dirname(__file__), '..', 'logs')
    file_name = os.path.join(logs_folder, f'{str(datetime.datetime.now().strftime('%d.%m.%Y.%H.%M.%S.'))}.log')

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Start time: {str(datetime.datetime.now())}\n'
        data_to_add += f'Start name method: {method}'
        data_to_add += '\n'

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, method: str):

        data_to_add = f'End time: {str(datetime.datetime.now())}\n'
        data_to_add += f'End name method: {method}\n'
        data_to_add += f'\n-----\n'

        cls.write_log_to_file(data_to_add)

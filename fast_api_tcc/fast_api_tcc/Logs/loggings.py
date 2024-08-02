import os
import uuid
from logging import DEBUG, basicConfig, error, getLogger


class Log:
    def __init__(self, logger_name):
        try:
            # Nome do arquivo de log
            log_filename = './fast_api_tcc/Logs/log_test.tsv'

            # Gera um hash único para a execução
            self.execution_key = self.new_key()

            # Adiciona cabeçalho e chave de execução se o arquivo não existir
            if not os.path.exists(log_filename):
                with open(log_filename, 'w', encoding='utf-8') as file:
                    file.write(
                        'Key Execution\tTimestamp\tLogger Name\tLine Number\tLog Level\tMessage\n'
                    )

            # Adiciona a chave de execução na primeira linha de
            # log de uma nova execução
            with open(log_filename, 'a', encoding='utf-8') as file:
                file.write(f'{self.execution_key}\t-\t-\t-\t-\tFirst Execution\n')

            # Configuração do logger
            basicConfig(
                level=DEBUG,
                filename=log_filename,
                filemode='a',
                encoding='utf-8',
                format=f'{self.execution_key}\t%(asctime)s\t%(name)s\t%(lineno)d\t%(levelname)s\t%(message)s',
            )

            # Obtém o logger especificado
            self.logger = getLogger(logger_name)

            self.log_start('Log criado com sucesso')
        except Exception as e:
            error(f'Erro ao criar o log: {e}')

    @staticmethod
    def new_key():
        return str(uuid.uuid4())

    def log_start(self, message='Início da execução'):
        self.logger.info(message)

    def log_end(self):
        self.logger.info('Fim da execução')

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)

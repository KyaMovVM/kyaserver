FileInputStream — декорируемый
компонент. Библиотека ввода/вывода Java предоставляет базовые компоненты FileInputStream,
StringBufferInputStream,
ByteArrayInputStream, предназначенные для чтения байтов данных.

BufferedInputStream
представляет собой
конкретный декоратор.
BufferedInputStream расширяет FileInputStream
поведением буферизации;
входные данные буферизуются для повышения
быстродействия.

Конкретный декоратор
LineNumberInputStream
добавляет возможность
подсчета строк в процессе
чтения данных.

BufferedInputStream и LineNumberInputStream расширяют FilterInputStream —
абстрактный класс декоратора.
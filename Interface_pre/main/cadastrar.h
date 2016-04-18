#ifndef CADASTRAR_H
#define CADASTRAR_H

#include <QMainWindow>

namespace Ui {
class cadastrar;
}

class cadastrar : public QMainWindow
{
    Q_OBJECT

public:
    explicit cadastrar(QWidget *parent = 0);
    ~cadastrar();

private:
    Ui::cadastrar *ui;
};

#endif // CADASTRAR_H

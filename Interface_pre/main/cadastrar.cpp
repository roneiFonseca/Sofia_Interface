#include "cadastrar.h"
#include "ui_cadastrar.h"

cadastrar::cadastrar(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::cadastrar)
{
    ui->setupUi(this);
}

cadastrar::~cadastrar()
{
    delete ui;
}

#include "monidialog.h"
#include "ui_monidialog.h"

moniDialog::moniDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::moniDialog)
{
    ui->setupUi(this);
    QPixmap pix("/home/pi/Teste2_interface/imagens/logo.png");
    ui->label->setPixmap(pix);
    this ->ui->lcdNumber_10->display(233);    //variavel de potencia
    this ->ui->lcdNumber_8->display(233);    //variavel de temperatura
    this ->ui->lcdNumber_9->display(233);   //variavel de impedancia
    this ->ui->lcdNumber_7->display(233);   //variavel de tempo
}

moniDialog::~moniDialog()
{
    delete ui;
}

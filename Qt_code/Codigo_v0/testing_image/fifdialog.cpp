#include "fifdialog.h"
#include "ui_fifdialog.h"

fifDialog::fifDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::fifDialog)
{
    ui->setupUi(this);
    QPixmap pix("/home/pi/Teste2_interface/imagens/logo.png");
    ui->label->setPixmap(pix);
}

fifDialog::~fifDialog()
{
    delete ui;
}

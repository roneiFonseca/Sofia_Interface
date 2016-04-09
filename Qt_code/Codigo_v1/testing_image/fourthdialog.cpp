#include "fourthdialog.h"
#include "ui_fourthdialog.h"

fourthDialog::fourthDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::fourthDialog)
{
    ui->setupUi(this);
    QPixmap pix("/home/pi/Teste2_interface/imagens/logo.png");
    ui->label->setPixmap(pix);
    this->connect(this->ui->pushButton, SIGNAL(clicked()), this,SLOT(button_Plus_click3()));
    this->connect(this->ui->pushButton_2, SIGNAL(clicked()), this,SLOT(button_Minus_click3()));
    this->counter3=10;
    this->ui->lcdNumber->display(counter3);

    this->connect(this->ui->pushButton_3, SIGNAL(clicked()), this,SLOT(button_Plus_click4()));
    this->connect(this->ui->pushButton_4, SIGNAL(clicked()), this,SLOT(button_Minus_click4()));
   // this->connect(this->ui->pushButton_5, SIGNAL(clicked()), this,SLOT(on_pushButton_5_clicked()));
    this->counter4=10;
    this->ui->lcdNumber_2->display(counter4);
}

fourthDialog::~fourthDialog()
{
    delete ui;
}

void fourthDialog::button_Minus_click3()
{
    counter3 --;
    this ->ui->lcdNumber->display(counter3);
    while (counter3 < 0){
        this ->ui->lcdNumber->display(0);
        counter3 = 0;
    }
}


void fourthDialog:: button_Plus_click3()
{
    counter3 ++;
    this ->ui->lcdNumber->display(counter3);
    while (counter3 > 50){
        this ->ui->lcdNumber->display(50);
        counter3 = 50;
    }
}

void fourthDialog::button_Minus_click4()
{
    counter4 --;
    this ->ui->lcdNumber_2->display(counter4);
    while (counter4 < 0){
        this ->ui->lcdNumber_2->display(0);
        counter4 = 0;
    }
}


void fourthDialog:: button_Plus_click4()
{
    counter4 ++;
    this ->ui->lcdNumber_2->display(counter4);
    while (counter4 > 50){
        this ->ui->lcdNumber_2->display(50);
        counter4 = 50;
    }

}

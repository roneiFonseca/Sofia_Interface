#include "thirddialog.h"
#include "ui_thirddialog.h"
#include "mainwindow.h"
#include "secdialog.h"

thirdDialog::thirdDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::thirdDialog)
{
    ui->setupUi(this);
    QPixmap pix("/home/pi/Teste2_interface/imagens/logo.png");
    ui->label->setPixmap(pix);
    this->connect(this->ui->pushButton, SIGNAL(clicked()), this,SLOT(button_Plus_click()));
    this->connect(this->ui->pushButton_2, SIGNAL(clicked()), this,SLOT(button_Minus_click()));
    this->counter=10;
    this->ui->lcdNumber->display(counter);

    this->connect(this->ui->pushButton_3, SIGNAL(clicked()), this,SLOT(button_Plus_click2()));
    this->connect(this->ui->pushButton_4, SIGNAL(clicked()), this,SLOT(button_Minus_click2()));
    this->connect(this->ui->pushButton_5, SIGNAL(clicked()), this,SLOT(on_pushButton_5_clicked()));
    this->counter2=10;
    this->ui->lcdNumber_2->display(counter2);
}

thirdDialog::~thirdDialog()
{
    delete ui;
}

void thirdDialog::button_Minus_click()
{
    counter --;
    this ->ui->lcdNumber->display(counter);
    while (counter < 0){
        this ->ui->lcdNumber->display(0);
        counter = 0;
    }
}


void thirdDialog:: button_Plus_click()
{
    counter ++;
    this ->ui->lcdNumber->display(counter);
    while (counter > 50){
        this ->ui->lcdNumber->display(50);
        counter = 50;
    }
}

void thirdDialog::button_Minus_click2()
{
    counter2 --;
    this ->ui->lcdNumber_2->display(counter2);
    while (counter2 < 0){
      this ->ui->lcdNumber_2->display(0);
        counter2 = 0;
    }
}


void thirdDialog:: button_Plus_click2()
{
    counter2 ++;
    this ->ui->lcdNumber_2->display(counter2);
   while (counter2 > 50){
        this ->ui->lcdNumber_2->display(50);
       counter2 = 50;
    }
}

void thirdDialog::on_pushButton_5_clicked()
{

}

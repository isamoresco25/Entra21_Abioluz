{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ex01.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNsnT+nIcUV2FZjClFaSfkV"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bTduWgpqNrIm",
        "outputId": "ced20c44-2b11-4ad3-be47-dbbe9e49aae7"
      },
      "source": [
        "# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, \n",
        "#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:\n",
        "\n",
        "#     salário bruto.\n",
        "#     quanto pagou ao INSS.\n",
        "#     quanto pagou ao sindicato.\n",
        "#     o salário líquido.\n",
        "#     calcule os descontos e o salário líquido, conforme a tabela abaixo: \n",
        "#     + Salário Bruto : R$\n",
        "#     - IR (11%) : R$\n",
        "#     - INSS (8%) : R$\n",
        "#     - Sindicato ( 5%) : R$\n",
        "#     = Salário Liquido : R$\n",
        "\n",
        "\n",
        "sal_hora = float(input('Digite o salário que você ganha por hora: '))\n",
        "\n",
        "num_horas = float(input('Digite quantas horas você trabalha por mês: '))\n",
        "\n",
        "sal_bruto = (sal_hora*num_horas)\n",
        "\n",
        "ir = (sal_bruto*(11/100))\n",
        "\n",
        "inss = (sal_bruto*(8/100))\n",
        "\n",
        "sindicato = (sal_bruto*(5/100))\n",
        "\n",
        "contas = ir+inss+sindicato\n",
        "\n",
        "sal_liq = sal_bruto - contas\n",
        "\n",
        "print(f''' {'='*30}\n",
        "+ Salário Bruto : R$ {sal_bruto}\n",
        "- IR (11%) : R$ {ir}\n",
        "- INSS (8%) : R$ {inss}\n",
        "- Sindicato ( 5%) : R$ {sindicato}\n",
        "= Salário Liquido : R$ {sal_liq}\n",
        "{'='*30}''')"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Digite o salário que você ganha por hora: 200\n",
            "Digite quantas horas você trabalha por mês: 200\n",
            " ==============================\n",
            "+ Salário Bruto : R$ 40000.0\n",
            "- IR (11%) : R$ 4400.0\n",
            "- INSS (8%) : R$ 3200.0\n",
            "- Sindicato ( 5%) : R$ 2000.0\n",
            "= Salário Liquido : R$ 30400.0\n",
            "==============================\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
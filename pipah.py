{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN2znbkL///yNPmv5V3yL0F",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/afifahyulfahazani/afifahyulfahazani/blob/master/pipah.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e4XM066uhdPz",
        "outputId": "92f06d81-87c2-4dea-a04a-e6fd08593b52"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Penjumlahan:\n",
            " [[ 6  8]\n",
            " [10 12]]\n",
            "\n",
            "Pengurangan:\n",
            " [[-4 -4]\n",
            " [-4 -4]]\n",
            "\n",
            "Perkalian:\n",
            " [[19 22]\n",
            " [43 50]]\n",
            "\n",
            "Transpose matriks1:\n",
            " [[1 3]\n",
            " [2 4]]\n"
          ]
        }
      ],
      "source": [
        "# prompt: buatkan kode python hitung matriks\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "# Buat matriks contoh\n",
        "matriks1 = np.array([[1, 2], [3, 4]])\n",
        "matriks2 = np.array([[5, 6], [7, 8]])\n",
        "\n",
        "# Penjumlahan matriks\n",
        "penjumlahan = matriks1 + matriks2\n",
        "print(\"Penjumlahan:\\n\", penjumlahan)\n",
        "\n",
        "# Pengurangan matriks\n",
        "pengurangan = matriks1 - matriks2\n",
        "print(\"\\nPengurangan:\\n\", pengurangan)\n",
        "\n",
        "# Perkalian matriks\n",
        "perkalian = np.dot(matriks1, matriks2)\n",
        "print(\"\\nPerkalian:\\n\", perkalian)\n",
        "\n",
        "# Transpose matriks\n",
        "transpose = matriks1.T\n",
        "print(\"\\nTranspose matriks1:\\n\", transpose)\n"
      ]
    }
  ]
}
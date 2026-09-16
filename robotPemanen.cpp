#include <iostream>
#include <vector>

using namespace std;

int main() {

	int M, N;
	cin >> M >> N;

	vector<vector<int>> tanaman(M, vector<int>(N));
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> tanaman[i][j];
		}
	}

	vector<int> beratKantong;
	int totalSaatIni = 0;
	int jumlahTanaman = 0;

	int atas = 0;
	int bawah = M - 1;
	int kiri = 0;
	int kanan = N - 1;

	auto panen = [&](int berat) {
		totalSaatIni += berat;
		++jumlahTanaman;

		if (jumlahTanaman == 10) {
			beratKantong.push_back(totalSaatIni);
			totalSaatIni = 0;
			jumlahTanaman = 0;
		}
	};

	while (atas <= bawah && kiri <= kanan) {
		for (int kolom = kiri; kolom <= kanan; ++kolom) {
			panen(tanaman[atas][kolom]);
		}
		++atas;

		for (int baris = atas; baris <= bawah; ++baris) {
			panen(tanaman[baris][kanan]);
		}
		--kanan;

		if (atas <= bawah) {
			for (int kolom = kanan; kolom >= kiri; --kolom) {
				panen(tanaman[bawah][kolom]);
			}
			--bawah;
		}

		if (kiri <= kanan) {
			for (int baris = bawah; baris >= atas; --baris) {
				panen(tanaman[baris][kiri]);
			}
			++kiri;
		}
	}

	if (jumlahTanaman > 0) {
		beratKantong.push_back(totalSaatIni);
	}

	cout << beratKantong.size() << '\n';
	for (size_t i = 0; i < beratKantong.size(); ++i) {
		if (i > 0) {
			cout << ' ';
		}
		cout << beratKantong[i];
	}
	cout << '\n';

	return 0;
}

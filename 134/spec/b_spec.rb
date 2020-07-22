require_relative '../b'

describe 'calculate_number_of_worker' do
  context '木が偶数本である場合' do
    context '監視範囲が奇数値である場合' do
      it '従業員が2人必要であること' do
        expect(calculate_number_of_worker(6,2)).to eq(2)
      end
    end
    context '監視範囲が偶数値である場合' do
      it '従業員が2人必要であること' do
        expect(calculate_number_of_worker(14,3)).to eq(2)
      end
    end
  end

  context '木が奇数本である場合' do
    context '監視範囲が奇数値である場合' do
      it '従業員が2人必要であること' do
        expect(calculate_number_of_worker(7,2)).to eq(2)
      end
    end
  
    context '監視範囲が偶数値である場合' do
      it '従業員が2人必要であること' do
        expect(calculate_number_of_worker(15,3)).to eq(3)
      end
    end
  end
end

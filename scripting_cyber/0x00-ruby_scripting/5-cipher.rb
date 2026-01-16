class CaesarCipher
  def initialize(shift)
    @shift = shift
  end

  def encrypt(message)
    cipher(message, @shift)
  end

  def decrypt(message)
    cipher(message, -@shift)
  end

  private

  def cipher(message, shift)
    result = ""

    message.each_char do |char|
      if char =~ /[A-Z]/    # Böyük hərflər
        result += ((char.ord - 65 + shift) % 26 + 65).chr
      elsif char =~ /[a-z]/ # Kiçik hərflər
        result += ((char.ord - 97 + shift) % 26 + 97).chr
      else
        result += char      # hərf olmayanları dəyişdirmə
      end
    end

    result
  end
end

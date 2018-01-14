function getCity(province) {
    if(province == 'vn-hanoi') {
        return ['Quận Ba Đình','Quận Hoàn Kiếm','Quận Tây Hồ','Quận Long Biên','Quận Cầu Giấy','Quận Đống Đa','Quận Hai Bà Trưng','Quận Hoàng Mai','Quận Thanh Xuân','Quận Hà Đông','Quận Bắc Từ Liêm','Quận Nam Từ Liêm','Thị xã Sơn Tây','Huyện Ba Vì','Huyện Chương Mỹ','Huyện Đan Phượng','Huyện Đông Anh','Huyện Gia Lâm','Huyện Hoài Đức','Huyện Mê Linh','Huyện Mỹ Đức','Huyện Phú Xuyên','Huyện Phúc Thọ','Huyện Quốc Oai','Huyện Sóc Sơn','Huyện Thạch Thất','Huyện Thanh Oai','Huyện Thanh Trì','Huyện Thường Tín','Huyện Ứng Hòa'];
    }
    else if(province == 'vn-hochiminh') {
        return ['Quận 1','Quận 2','Quận 3','Quận 4','Quận 5','Quận 6','Quận 7','Quận 8','Quận 9','Quận 10','Quận 11','Quận 12','Quận Thủ Đức','Quận Tân Phú','Quận Tân Bình','Quận Phú Nhuận','Quận Gò Vấp','Quận Bình Thạnh','Quận Bình Tân','Huyện Bình Chánh','Huyện Cần Giờ','Huyện Củ Chi','Huyện Hóc Môn','Huyện Nhà Bè'];
    }
    else if(province == 'vn-danang') {
        return ['Quận Hải Châu','Quận Cẩm Lệ','Quận Thanh Khê','Quận Liên Chiểu','Quận Ngũ Hành Sơn','Quận Sơn Trà','Huyện Hòa Vang','Huyện đảo Hoàng Sa'];
    }
    else if(province == 'vn-cantho') {
        return ['Quận Ninh Kiều','Quận Bình Thủy','Quận Cái Răng','Quận Ô Môn','Quận Thốt Nốt','Quận Phong Điền','Quận Cờ Đỏ','Quận Thới Lai','Quận Vĩnh Thạnh'];
    }
    else if(province == 'vn-haiphong') {
        return ['Quận Dương Kinh','Quận Đồ Sơn','Quận Hải An','Quận Kiến An','Quận Hồng Bàng','Quận Ngô Quyền','Quận Lê Chân','Huyện An Dương','Huyện An Lão','Huyện đạo Bạch Long Vĩ','Huyện đảo Cát Hải','Huyện Kiến Thụy','Huyện Tiên Lãng','Huyện Vĩnh Bảo','Huyện Thủy Nguyên'];
    }
    else if (province === 'vn-brvt') {
        return ['Thành phố Vũng Tàu','Thành phố Bà Rịa','Huyện Châu Đức','Huyện đảo Côn Đảo','Huyện Đất Đỏ','Huyện Long Điền','Huyện Tân Thành','Huyện Xuyên Mộc'];
    }
    else if(province === 'vn-quangtri') {
        return ['Thành phố Đông Hà','Thị xã Quảng Trị','Huyện Cam Lộ','Huyện Cồn Cỏ','Huyện Đa Krông','Huyện Gio Linh','Huyện Hải Lăng','Huyện Hướng Hóa','Huyện Triệu Phong','Huyện Vĩnh Linh'];
    }
    else if(province == 'vn-angiang') {
        return ['Thành phố Long Xuyên','Thành phố Châu Đốc','Thị xã Tân Châu','Huyện An Phú','Huyện Châu Phú','Huyện Châu Thành','Huyện Chợ Mới','Huyện Phú Tân','Huyện Thoại Sơn','Huyện Tịnh Biên','Huyện Tri Tôn'];
    }
    else if (province == 'vn-bacgiang') {
        return ['Thành phố Bắc Giang','Huyện Yên Thế','Huyện Tân Yên','Huyện Lục Ngạn','Huyện Hiệp Hòa','Huyện Lạng Giang','Huyện Sơn Động','Huyện Lục Nam','Huyện Việt Yên','Huyện Yên Dũng'];
    }
    else if(province == 'vn-backan') {
        return ['Thành phố Bắc Kạn','Huyện Ba Bể','Huyện Bạch Thông','Huyện Chợ Đồn','Huyện Chợ Mới','Huyện Na Rì','Huyện Ngân Sơn','Huyện Pác Nặm'];
    }
    else if(province == 'vn-baclieu') {
        return ['Thành phố Bạc Liêu','Thị xã Giá Rai','Huyện Hồng Dân','Huyện Hòa Bình','Huyện Phước Long','Huyện Vĩnh Lợi','Huyện Đông Hải'];
    }
    else if(province == 'vn-bacninh') {
        return ['Thành phố Bắc Ninh','Thị xã Từ Sơn','Huyện Gia Bình','Huyện Lương Tài','Huyện Quế Võ','Huyện Thuận Thành','Huyện Tiên Du','Huyện Yên Phong'];
    }
    else if(province == 'vn-bentre') {
        return ['Thành phố Bến Tre','Huyện Ba Tri','Huyện Bình Đại','Huyện Châu Thành','Huyện Chợ Lách','Huyện Giồng Trôm','Huyện Mỏ Cày Bắc','Huyện Mỏ Cày Nam','Huyện Thạnh Phú'];
    }
    else if(province == 'vn-binhdinh') {
        return ['Thành phố Quy Nhơn','Thị xã An Nhơn','Huyện Hoài Nhơn','Huyện An Lão','Huyện Phù Cát','Huyện Phù Mỹ','Huyện Tuy Phước','Huyện Tây Sơn','Huyện Vân Canh','Huyện Vĩnh Thạnh','Huyện Hoài Ân'];
    }
    else if(province == 'vn-binhduong') {
        return ['Thành phố Thủ Dầu Một','Thị xã Thuận An','Thị xã Dĩ An','Thị xã Bến Cát','Thị xã Tân Uyên','Huyện Dầu Tiếng','Huyện Phú Giáo','Huyện Bàu Bàng','Huyện Bắc Tân Uyên'];
    }
    else if(province == 'vn-binhphuoc') {
        return ['Thị xã Đồng Xoài','Thị xã Bình Long','Thị xã Phước Long','Huyện Bù Đăng','Huyện Bù Đốp','Huyện Bù Gia Mập','Huyện Chơn Thành','Huyện Đồng Phú','Huyện Hớn Quản','Huyện Lộc Ninh','Huyện Phú Riềng'];
    }
    else if(province =='vn-binhthuan') {
        return ['Thành phố Phan Thiết','Thị xã La Gi','Huyện Tuy Phong','Huyện Bắc Bình','Huyện Hàm Thuận Bắc','Huyện Hàm Thuận Nam','Huyện Tánh Linh','Huyện Hàm Tân','Huyện Đức Linh','Huyện Phú Quý'];
    }
    else if(province == 'vn-camau') {
        return ['Thành phố Cà Mau','Huyện Đầm Dơi','Huyện Ngọc Hiển','Huyện Cái Nước','Huyện Trần Văn Thời','Huyện U Minh','Huyện Thới Bình','Huyện Năm Căn','Huyện Phú Tân'];
    }
    else if(province == 'vn-caobang') {
        return ['Thành phố Cao Bằng','Huyện Bảo Lạc','Huyện Bảo Lâm','Huyện Hà Lang','Huyện Hà Quảng','Huyện Hòa An','Huyện Nguyên Bình','Huyện Phục Hòa','Huyện Quảng Uyên','Huyện Thạch An','Huyện Thông Nông','Huyện Trà Lĩnh','Huyện Trùng Khánh'];
    }
    else if(province == 'vn-daklak') {
        return ['Thành phố Buôn Ma Thuột','Thị xã Buôn Hồ','Huyện Ea Súp','Huyện Krông Bông','Huyện Krông Buk','Huyện Krông Pak','Huyện Krông Năng','Huyện Krông Ana','Huyện M\'Drăk','Huyện Lắk','Huyện Ea Kar','Huyện Ea Kar',"Huyện Ea H'leo",'Huyện Cư M\'gar','Huyện Cư Kuin','Huyện Buôn Đôn'];
    }
    else if(province == 'vn-dacnong') {
        return ['Thị xã Gia Nghĩa','Huyện Cư jút','Huyện Đắk Giong','Huyện Đắk Mil','Huyện Đắk R\'lấp','Huyện Đắk Song','Huyện Krông Nô','Huyện Tuy Đức'];
    }
    else if(province == 'vn-dienbien') {
        return ['Thành phố Điện Biên Phủ','Thị xã Mường Lay','Huyện Điện Biên','Huyện Mường Ảng','Huyện Mường Chà','Huyện Mường Nhé','Huyện Tủa Chùa','Huyện Tuần Giáo','Huyện Nậm Pồ'];
    }
    else if(province == 'vn-dongnai') {
        return ['Thị xã Biên Hòa','Thị xã Long Khánh','Huyện Long Thành','Huyện Nhơn Trạch','Huyện Trảng Bom','Huyện Thồng Nhất','Huyện Vĩnh Cửu','Huyện Cẩm Mỹ','Huyện Xuân Lộc','Huyện Tân Phú','Huyện Định Quán'];
    }
    else if(province == 'vn-dongthap') {
        return ['Thành phố Cao Lãnh','Thành phố Sa Đéc','Thị Xã Hồng Ngự','Huyện Cao Lãnh','Huyện Châu Thành','Huyện Hồng Ngự','Huyện Lai Vung','Huyện Lấp Vó','Huyện Tam Nông','Huyện Tân Hồng','Huyện Thanh Bình','Huyện Tháp Mười'];
    }
    else if(province == 'vn-gialai') {
        return ['Thành phố Pleiku','Thị xã An Khê','Thị xã Ayun Pa','Huyện Chư Păh','Huyện Chư Prông','Huyện Chư Sệ','Huyện Đắk Đoa','Huyện Chư Pưh','Huyện Phú Thiện','Huyện Mang Yang','Huyện Krông Pa','Huyện Kông Chro','Huyện Ia Pa','Huyện Ia Grai','Huyện Đức Cơ','Huyện Đak Pơ'];
    }
    else if(province == 'vn-hanam') {
        return ['Thành phố Phủ Lý','Huyện Duy Tiên','Huyện Kim Bảng','Huyện Lý Nhân','Huyện Thanh Liêm','Huyện Bình Lục'];
    }
    else if(province == 'vn-hagiang') {
        return ['Thành phố Hà Giang','Huyện Bắc Mê','Huyện Bắc Quang','Huyện Đồng Văn','Huyện Hoàng Su Phì','Huyện Mèo Vạc','Huyện Quản Bạ','Huyện Quang Bình','Huyện vị Xuyên','Huyện Xín Mần','Huyện Yên Minh'];
    }
    else if(province == 'vn-hatinh') {
        return ['Thành phố Hà Tĩnh','Thị xã Hồng Lĩnh','Thị xã Kỳ Anh','Huyện Cẩm Xuyên','Huyện Can Lộc','Huyện Đức Thọ','HUyện Hương Khê','Huyện Hương Sơn','Huyện Kỳ Anh','Huyện Nghi Xuân','Huyện Thạch Hà','Huyện Vũ Quang','Huyện Lộc Hà'];
    }
    else if(province == 'vn-haiduong') {
        return ['Thành phố Hải Dương','Thị xã Chí Linh','Huyện Bình Giang','Huyện Cẩm Giàng','Huyện Gia Lộc','Huyện Kim Thành','Huyện Kinh Môn','Huyện Nam Sách','Huyện Ninh Giang','Huyện Thanh Hà','Huyện Thanh Miện','Huyện Tứ Kỳ'];
    }
    else if(province == 'vn-haugiang') {
        return ['Thành phố Vị Thanh','Thị xã Long Mỹ','Thị xã Ngã bảy','Huyện Châu Thành','Huyện Châu Thành A','Huyện Long Mỹ','Huyện Phụng Hiệp','Huyện Vị Thủy'];
    }
    else if(province == 'vn-hoabinh') {
        return ['Thành phố Hòa Bình','Huyện Lương Sơn','Huyện Cao Phong','Huyện Đà Bắc','Huyện Kim Bội','Huyện Kỳ Sơn','Huyện Lạc Sơn','Huyện Lạc Thủy','Huyện Mai Châu','Huyện Tân Lạc','Huyện Yên Thủy'];
    }
    else if(province == 'vn-hungyen') {
        return ['Thành phố Hưng Yên','Huyện Ân Thị','Huyện Khoái Châu','Huyện Kim Động','Huyện Mỹ Hào','Huyện Phù Cư','Huyện Tiên Lữ','Huyện Văn Giang','Huyện Văn Lâm','Huyện Yên Mỹ'];
    }
    else if(province == 'vn-khanhhoa') {
        return ['Thành phố Nha Trang','Thành phố Cam Ranh','Thị xã Ninh Hòa','Huyện Vạn Ninh','Huyện Diên Khánh','Huyện Khánh Vinh','Huyện Khánh Sơn','Huyện Cam Lâm','Huyện đảo Trường Sa'];
    }
    else if(province == 'vn-kiengiang') {
        return ['Thành phố Rạch Giá','Thị xã Hà Tiên','Huyện An Biên','Huyện An Minh','Huyện Châu Thành','Huyện Giống Riềng','Huyện Giang Thành','Huyện Gò Quao','Huyện Hòn Đất','Huyện U Minh Thượng','Huyện Kiên Lương','Huyện Tân Hiệp','Huyện Vĩnh Thuận','Huyện đảo Kiên Hải','Huyện đảo Phú Quốc'];
    }
    else if(province == 'vn-kontum') {
        return ['Thành phố Kon Tum','Huyện Đắk Glei','Huyện Đắk Hà','Huyện Đắk Tô','Huyện la H\'Drai','Huyện Kon Plông','Huyện Kon Rây','Huyện Ngọc Hồi','Huyện Sa Thầy','Huyện Tu Mơ Rông'];
    }
    else if(province == 'vn-laichau') {
        return ['Thành phố Lai Châu','Huyện Mường Tè','Huyện Phong Thổ','Huyện Sìn Hồ','Huyện Than Uyên','Huyện Tam Đường','Huyện Tân Uyên','Huyện Nậm Nhùn'];
    }
    else if(province == 'vn-langson') {
        return ['Thành phố Lạng Sơn','Huyện Bắc Sơn','Huyện Bình Gia','Huyện Cao Lộc','Huyện Chi Lăng','Huyện Đình Lập','Huyện Hữu Lũng','Huyện Lộc Bình','Huyện Tràng Định','Huyện Văn Lãng','Huyện Văn Quan'];
    }
    else if(province == 'vn-laocai') {
        return ['Thành phố Lào Cai','Huyện Bảo Thắng','Huyện Bảo Yên','Huyện Bát Xát','Huyện Bắc Hà','Huyện Mường Khương','Huyện SaPa','Huyện Si Ma Cai','Huyện Văn Bàn'];
    }
    else if(province == 'vn-lamdong') {
        return ['Thành phố Đà Lạt','Thành phố Bảo Lộc','Huyện Bảo Lâm','Huyện Cát Tiên','Huyện Di Linh','Huyện Đam Rông','Huyện Đạ Huoai','Huyện Đạ Tẻh','Huyện Đơn Dương','Huyện Lạc Dương','Huyện Lâm Hà','Huyện Đức Trọng'];
    }
    else if(province == 'vn-longan') {
        return ['Thành phố Tân An','Thị xã Kiến Tường','Huyện Bến Lức','Huyện Cần Đước','Huyện Cần Giuộc','Huyện Châu Thành','Huyện Đức Huệ','Huyện Mộc Hóa','Huyện Tân Hưng','Huyện Tân Thạnh','Huyện Tân Trụ','Huyện Thạnh Hóa','Huyện Thủ Thừa','Huyện Vĩnh Hưng','Huyện Đức Hòa'];
    }
    else if(province == 'vn-namdinh') {
        return ['Thành phố Nam Định','Huyện Giao Thủy','Huyện Hải Hậu','Huyện Mỹ Lộc','Huyện Nam Trực','Huyện Nghĩa Hưng','Huyện Trực Ninh','Huyện Vụ Bản','Huyện Xuân Trường','Huyện Ý Yên'];

    }
    else if(province == 'vn-nghean') {
        return ['Thành phố Vinh','Thị xã Cửa Lò','Thị xã Hoàng Mai','Thị xã Thái Hòa','Huyện Anh Sơn','Huyện Con Cuông','Huyện Diễn Châu','Huyện Đô Lương','Huyện Hưng Nguyên','Huyện Quỳ Châu','Huyện Kỳ Sơn','Huyện Nam Đàn','Huyện Nghi Lộc','Huyện Quế Phong','Huyện Qùy Hợp','Huyện Quỳnh Lưu','Huyện Tân Kỳ','Huyện Thanh Chương','Huyện Tương Dương','Huyện Yên Thành'];
    }
    else if(province == 'vn-ninhbinh') {
        return ['Thành phố Ninh Bình','Thành phố Tam Điệp','Huyện Gia Viễn','HUyện Hoa Lư','Huyện Kim Sơn','Huyện Nho Quan','Huyện Yên Khánh','Huyện Yên Mô'];
    }
    else if(province == 'vn-ninhthuan') {
        return ['Thành phố Phan Rang - Tháp Chàm','Huyện Bác Ái','Huyện Ninh Hải','Huyện Ninh Phước','Huyện Ninh Sơn','Huyện Thuận Bắc','Huyện Thuận Nam'];
    }
    else if(province == 'vn-phutho') {
        return ['Thành phố Việt Trì','Thị xã Phú Thọ','Huyện Cẩm Khê','Huyện Đoan Hùng','Huyện Hạ Hòa','Huyện Lâm Thao','Huyện Phù Ninh','Huyện Tam Nông','Huyện Tân Sơn','Huyện Thanh Ba','Huyện Thanh Sơn','Huyện Thanh Thủy','Huyện Yên Lập'];
    }
    else if(province == 'vn-phuyen') {
        return ['Thành phố Tuy Hòa','Thị xã Sông Cầu','Huyện Đông Hòa','Huyện Đồng Xuân','Huyện Phú Hòa','Huyện Sơn Hòa','Huyện Sông Hinh','Huyện Tuy An','Huyện Tây Hòa'];
    }
    else if(province == 'vn-quangbinh') {
        return ['Thành phố Đồng Hới','Thị xã Ba Đồn','Huyện Minh Hóa','Huyện Tuyên Hóa','Huyện Quảng Trạch','Huyện Bố Trạch','Huyện Quảng Ninh','Huyện Lệ Thủy'];
    }
    else if(province == 'vn-quangnam') {
        return ['Thành phố Tam Kỳ','Thành phố Hội An','Thị xã Điện Bàn','Huyện Thăng Bình','Huyện Bắc Trà My','Huyện Nam Trà My','Huyện Núi Thành','Huyện Phước Sơn','HUyện Tiên Phước','Huyện Hiệp Đức','Huyện Nông Sơn','Huyện Đông Giang','Huyện Nam Giang','Huyện Đại Lộc','Huyện Phú Ninh','Huyện Tây Giang','Huyện Duy Xuyên','Huyện Quế Sơn'];
    }
    else if(province == 'vn-quangngai') {
        return ['Thành phố Quảng Ngãi','Huyện Ba Tơ','Huyện Bình Sơn','Huyện Đức Phố','Huyện Minh Long','Huyện Mộ Đức','Huyện đảo Lý Sơn','Huyện Tư Nghĩa','Huyện Trà Bồng','Huyện Tây Trà','Huyện Sơn Tịnh','Huyện Sơn Tây','Huyện Sơn Hà','Huyện Nghĩa Hành'];
    }
    else if(province == 'vn-quangninh') {
        return ['Thành phố Hạ Long','Thành phố Móng Cái','Thành phố Uông Bí','Thành phố Cẩm Phả','Thị xã Quảng Yên','Thị xã Đông Triều','Huyện Vân Đồn','Huyện Hoành Bồ','Huyện Đầm Hà','Huyện Cô Tô','Huyện Tiền Yên','Huyện Hải Hà','Huyện Bình Liêu','Huyện Ba Chẽ'];
    }
    else if(province == 'vn-soctrang') {
        return ['Thành phố Sóc Trăng','Thị xã Vĩnh Châu','Thị xã Ngã Năm','Huyện Long Phú','Huyện Kế Sách','Huyện Mỹ Tú','Huyện Mỹ Xuyên','Huyện Trần Đê','Huyện Thạch Trị','Huyện Châu Thành','Huyện Cù Lao Dung']
    }
    else if(province == 'vn-sonla') {
        return ['Thành phố Sơn La','Huyện Quỳnh Nhai','Huyện Mường La','HUyện Thuận Châu','Huyện Phú Yên','Huyện Bắc Yên','Huyện Mai Sơn','Huyện Sông Mã','Huyện Yên Châu','Huyện Mộc Châu','Huyện Sốp Cộp','Huyện Vân Hồ'];
    }
    else if(province == 'vn-tayninh') {
        return ['Thành phố Tây Ninh','Huyện Tân Biên','Huyện Tân Châu','Huyện Dương Minh Châu','Huyện Châu Thành','Huyện Hòa Thành','Huyện Bến Cầu','Huyện Gò Dầu','Huyện Trảng Bàng'];
    }
    else if(province == 'vn-thaibinh') {
        return ['Thành phố Thái Bình','Huyện Đông Hưng','Huyện Hưng Hà','Huyện Kiến Xương','Huyện Quỳnh Phụ','Huyện Tiền Hải','Huyện Thái Thụy','Huyện Vũ Thư'];
    }
    else if(province == 'vn-thainguyen') {
        return ['Thành phố Thái Nguyên','Thành phố Sông Công','Thị xã Phổ Yên','Huyện Đại Từ','Huyện Đồng Hỷ','Huyện Định Hóa','Huyện Phú Bình','Huyện Phú Lương','Huyện Võ Nhai'];
    }
    else if(province == 'vn-thanhhoa') {
        return ['Thành phố Thanh Hóa','Thị xã Bỉm Sơn','Thị xã Sầm Sơn','Huyện Bá Thước','HUyện Cầm Thủy','Huyện Đông Sơn','Huyện Hà Trung','Huyện Hậu Lộc','Huyện Hoằng Hóa','Huyện Lang Chánh','Huyện Mường Lát','Huyện Nga Sơn','Huyện Ngọc Lặc','Huyện Như Thanh','Huyện Như Xuân','Huyện Nông Cống','Huyện Quan Hóa','Huyện Quan Sơn','Huyện Quảng Xương','Huyện Thạch Thành','Huyện Thiệu Hóa','Huyện Thọ Xuân','Huyện Thường Xuân','Huyện Tĩnh Gia','Huyện Triệu Sơn','Huyện Vĩnh Lộc','Huyện Yên Định'];
    }
    else if(province == 'vn-hue') {
        return ['Thành phố Huế','Thị xã Hương Thủy','Thị xã Hương Trà','Huyện Phú Vang','Huyện Quảng Điền','Huyện A Lưới','Huyện Nam Đông','Huyện Phong Điền','Huyện Phú Lộc'];
    }
    else if(province == 'vn-tiengiang') {
        return ['Thành phố Mỹ Tho','Thị xã Gò Công','Thị xã Cai Lậy','Huyện Gò Công Đông','Huyện Cái Bè','Huyện Chợ Gạo','Huyện Châu Thành','Huyện Tân Phước','Huyện Cai Lậy','Huyện Tân Phú Đông'];
    }
    else if(province == 'vn-travinh') {
        return ['Thành phố Trà Vinh','Thị xã Duyên Hải','Huyện Càng Long','Huyện Cầu Kè','Huyện Tiểu Cần','Huyện Châu Thành','Huyện Cầu Ngang','Huyện Trà Cú','Huyện Duyên Hải'];
    }
    else if(province == 'vn-tuyenquang') {
        return ['Thành phố Tuyên Quang','Huyện Chiêm Hóa','Huyện Hàm Yên','Huyện Lâm Bình','Huyện Na Hang','Huyện Sơn Dương','Huyện Yên Sơn'];
    }
    else if(province == 'vn-vinhlong') {
        return ['Thành phố Vĩnh Long','Thị xã Bình Minh','Huyện Bình Tân','Huyện Long Hổ','Huyện Mang Thít','Huyện Tam Bình','Huyện Trà Ôn','Huyện Vũng Liêm'];
    }
    else if(province == 'vn-vinhphuc') {
        return ['Thành phố Vĩnh Yên','Thị xả Phúc Yên','Huyện Lập Thành','Huyện Bình Xuyên','Huyện Sông Lô','Huyện Tam Dương','Huyện Tam Đảo','Huyện Vĩnh Tường','Huyện Yên Lạc'];
    }
    else if(province == 'vn-yenbai') {
        return ['Thành phố Yên Bái','Thị xã Nghĩa Lộ','Huyện Lục Yên','Huyện Mù Cang Chải','Huyện Trạm Tấu','Huyện Trấn Yên','Huyện Văn Chấn','Huyện Văn Yên','Huyện Yên Bình'];
    }
    else {
        return null;
    }
}

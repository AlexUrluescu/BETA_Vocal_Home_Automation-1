import React from "react";

const StatusHeating = ({ isToggled, textStyle, text1, text2}) => {
  return (
    <div>
      {isToggled === true ? (
        <h2 className={textStyle}>{text1}</h2>
      ) : (
        <h2 className={textStyle}>{text2}</h2>
      )}
    </div>
  );
};

export default StatusHeating;
